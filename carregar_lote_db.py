import sqlite3
import csv
import os
import json

db_path = r'C:\IOTEC\iotec.db'
csv_path = r'C:\IOTEC\base_empresas.csv'
pointer_path = r'C:\IOTEC\ponteiro.json'

def carregar_ponteiro():
    if os.path.exists(pointer_path):
        try:
            with open(pointer_path, 'r') as f:
                return json.load(f)
        except:
            pass
    return {'offset_vendas': 0, 'offset_leads': 0, 'offset_legado': 0}

def salvar_ponteiro(p):
    with open(pointer_path, 'w') as f:
        json.dump(p, f)

def carregar_tanque_completo(limite_por_fonte=100):
    if not os.path.exists(db_path):
        print('[ERRO] Banco iotec.db nao localizado.')
        return

    p = carregar_ponteiro()
    lote_intercalado = []

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 1. FONTE: central_vendas_leads
        cursor.execute("SELECT razao_social, telefone FROM central_vendas_leads WHERE telefone IS NOT NULL AND length(telefone) >= 8 LIMIT ? OFFSET ?", (limite_por_fonte, p['offset_vendas']))
        vendas = cursor.fetchall()
        p['offset_vendas'] += len(vendas)

        # 2. FONTE: leads (187k)
        cursor.execute("SELECT company, id FROM leads WHERE company IS NOT NULL LIMIT ? OFFSET ?", (limite_por_fonte, p['offset_leads']))
        leads_gerais = cursor.fetchall()
        p['offset_leads'] += len(leads_gerais)

        conn.close()

        # Intercala os registros no lote
        max_len = max(len(vendas), len(leads_gerais))
        for i in range(max_len):
            if i < len(vendas):
                nome = vendas[i][0] if vendas[i][0] else "Empresa Alvo"
                lote_intercalado.append((nome, vendas[i][1]))
            if i < len(leads_gerais):
                nome = leads_gerais[i][0] if leads_gerais[i][0] else "Corporacao Global"
                lote_intercalado.append((nome, "5511999999999")) # Ajusta se houver telefone no legado

        if lote_intercalado:
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(['NomeEmpresa', 'Telefone', 'Status', 'DataContato'])
                for item in lote_intercalado:
                    writer.writerow([item[0], item[1], 'NOVO', ''])

            salvar_ponteiro(p)
            print(f'[?] COMBUSTIVEL REABASTECIDO: {len(lote_intercalado)} leads intercalados adicionados a esteira!')
            print(f'[->] Progresso atual do tanque: Vendas Offset={p["offset_vendas"]} | Leads Offset={p["offset_leads"]}')
        else:
            print('[!] Fim do reservatorio: Todos os registros do banco foram processados!')

    except Exception as e:
        print(f'[ERRO BANCO] Falha ao intercalar banco: {e}')

if __name__ == '__main__':
    carregar_tanque_completo(100)
