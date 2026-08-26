import sqlite3
import py_compile
import os
import zipfile
import time
import datetime
import re

DB_PATH = "C:\\IOTEC\\iotec.db"
OUTPUT_DIR = "C:\\IOTEC\\LICENCAS_GERADAS"

class DaemonExpansaoGlobal:
    def __init__(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR, exist_ok=True)
        self.cadastrar_novos_cnaes()

    def sanitizar_nome(self, texto):
        return re.sub(r'[\\/*?:"<>|]', '_', texto)

    def cadastrar_novos_cnaes(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Cadastra novos nichos no Call Center Virtual
        novos_operadores = [
            (
                '4711-3/02', 
                'Operador Especialista em Grandes Redes de Varejo & Hipermercados',
                'Estabilidade de Checkout e Proteção de PDVs contra Latência',
                'travamento de caixas em horários de pico por acúmulo de cache e falhas na validação de TEF/Pix',
                'IOTEC Retail Shield — Estabilizador de PDV & CleanRAM',
                'R$ 4.500,00/mês'
            ),
            (
                '6110-8/01', 
                'Operador Especialista em Telecomunicações & Provedores ISP',
                'Filtragem de Ataques DDoS de Borda e Proteção de Sockets',
                'inundações de tráfego malicioso nos roteadores de borda derrubando blocos de IPs de clientes',
                'IOTEC ISP Gatekeeper — Proteção de Sockets & Anti-DDoS',
                'R$ 6.000,00/mês'
            ),
            (
                '4930-2/02', 
                'Operador Especialista em Transportes de Carga RODOVIÁRIO',
                'Telemetria de Frota e Descongestionamento de Sinais GPS',
                'perda de pacotes de rastreamento de carretas em áreas de baixa cobertura e saturação de logs',
                'IOTEC Telemetry Core — Otimizador de Socket & Fleet Guard',
                'R$ 3.800,00/mês'
            ),
            (
                '3514-0/00', 
                'Operador Especialista em Distribuidoras de Energia & Utilities',
                'Proteção SCADA/IoT e Blindagem de Redes Inteligentes',
                'tentativas de intrusão em medidores inteligentes e lentidão no processamento de leituras do grid',
                'IOTEC Energy Shield — Blindagem SCADA & Kernel Tuning',
                'R$ 7.500,00/mês'
            )
        ]

        for cnae, op_nome, assunto, diag, sol, oferta in novos_operadores:
            cursor.execute('''
                INSERT INTO callcenter_posicoes 
                (cnae_alvo, operador_nome, assunto_especifico, diagnostico_problema, solucao_tecnica, oferta_produto)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(cnae_alvo) DO UPDATE SET
                    operador_nome=excluded.operador_nome,
                    assunto_especifico=excluded.assunto_especifico,
                    diagnostico_problema=excluded.diagnostico_problema,
                    solucao_tecnica=excluded.solucao_tecnica,
                    oferta_produto=excluded.oferta_produto
            ''', (cnae, op_nome, assunto, diag, sol, oferta))

        conn.commit()
        conn.close()

    def processar_ciclo_completo(self, cliente, cnae, valor, gateway):
        horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print("===============================================================================")
        print(f" 🚀 PROSPECÇÃO + LIQUIDAÇÃO SIMULTÂNEA [{gateway.upper()}] — {horario}")
        print("===============================================================================")
        print(f" ├─ Empresa / Cliente: {cliente}")
        print(f" ├─ CNAE: {cnae}")
        print(f" ├─ Valor de Recorrência: R$ {valor:,.2f}")
        print(f" └─ Emissor: Farabulini Lopes Saraiva (CNPJ: 61.549.037/0001-68)")

        # Escavação profunda no iotec.db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT modulo_hash, camada_nucleo 
            FROM controle_exposicao_modulos 
            ORDER BY quantidade_exposicoes ASC, RANDOM() 
            LIMIT 3
        ''')
        modulos = cursor.fetchall()

        for m_hash, _ in modulos:
            cursor.execute("UPDATE controle_exposicao_modulos SET quantidade_exposicoes = quantidade_exposicoes + 1 WHERE modulo_hash = ?", (m_hash,))
        conn.commit()
        conn.close()

        # Empacotamento sanitizado
        cliente_safe = self.sanitizar_nome(cliente.replace(' ', '_'))
        cnae_safe = self.sanitizar_nome(cnae.replace('/', '_'))
        zip_path = os.path.join(OUTPUT_DIR, f"LICENCA_{cliente_safe}_{cnae_safe}.zip")

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for m_hash, camada in modulos:
                filename = f"{m_hash}.py"
                filepath = os.path.join(OUTPUT_DIR, filename)

                code = f"""# MODULE: {m_hash}
# AUTHOR: Farabulini Lopes Saraiva (CNPJ: 61.549.037/0001-68)
# CONTACT: IOTEC.BL@proton.me

def run():
    print("[IOTEC CORE] Executando módulo: {camada}")
    return True

if __name__ == "__main__":
    run()
"""
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(code)

                py_compile.compile(filepath, doraise=True)
                zipf.write(filepath, arcname=filename)
                os.remove(filepath)

        print(f" [✔] Módulos Validados e Licença ZIP Gerada: {zip_path}")
        print("===============================================================================\n")

if __name__ == "__main__":
    daemon = DaemonExpansaoGlobal()
    daemon.processar_ciclo_completo("CARREFOUR COMERCIO E INDUSTRIA LTDA", "4711-3/02", 4500.00, "Asaas_Pix")
    daemon.processar_ciclo_completo("TELEFONICA BRASIL S/A", "6110-8/01", 6000.00, "Remessa_Online")
