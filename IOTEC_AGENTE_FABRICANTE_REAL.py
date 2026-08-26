import sqlite3
import json
import time
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

class AgenteArquitetoConsultivo:
    def __init__(self, lead_id, razao_social, relato_dor):
        self.lead_id = lead_id
        self.razao_social = razao_social
        self.relato = relato_dor.lower() if relato_dor else ""
        self.modulos = []
        self.diagnostico_humano = ""

    def analisar_dor_isolada(self):
        relato_txt = self.relato
        razao_txt = self.razao_social.lower()

        if any(w in relato_txt for w in ["rota", "frota", "combustivel", "entrega", "logistica"]) or "logística" in razao_txt or "transporte" in razao_txt:
            self.modulos = ["GESTAO_DE_FROTA_GPS", "ROTEAR_ENTREGAS", "CONTROLE_COMBUSTIVEL"]
            self.diagnostico_humano = "Analisamos seus gargalos operacionais de transporte e desenhamos um núcleo focado em redução de custos com frotas e otimização de rotas."

        elif any(w in relato_txt for w in ["obra", "material", "medicao", "construcao", "projeto"]) or "engenharia" in razao_txt or "construção" in razao_txt or "obras" in razao_txt:
            self.modulos = ["MEDICAO_DE_OBRAS", "GESTAO_INSUMOS", "CRONOGRAMA_FINANCEIRO"]
            self.diagnostico_humano = "Identificamos a necessidade de controle rígido do canteiro de obras, estimativa de insumos e alocação financeira por projeto."

        elif any(w in relato_txt for w in ["venda", "cliente", "lead", "comissao", "crm"]) or "comercial" in razao_txt or "distribuidora" in razao_txt:
            self.modulos = ["CRM_PREDITIVO", "PIPELINE_VENDAS", "CALCULO_COMISSOES_AUTO"]
            self.diagnostico_humano = "Desenhamos uma estrutura focada em acelerar seu funil comercial, prever vendas e automatizar acertos de comissão."

        elif any(w in relato_txt for w in ["caixa", "faturamento", "nota", "cobrança", "banco"]) or "financeiro" in razao_txt:
            self.modulos = ["TESOURARIA_AVANCADA", "GATEWAY_COBRANCA_AUTO", "CONCILIACAO_BANCARIA"]
            self.diagnostico_humano = "Configuramos uma tesouraria autônoma focada em zerar inadimplência e automatizar relatórios de fluxo de caixa."

        else:
            self.modulos = ["NÚCLEO_OPERACIONAL_MODULAR", "PAINEL_DECISORIO_EXECUTIVO"]
            self.diagnostico_humano = "Criamos uma arquitetura sob medida para otimização dos processos internos e controle de indicadores da sua empresa."

    def fabricar_solucao_unica(self):
        horario = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"\n[{horario}] [⚡ SISTEMA EM FABRICAÇÃO — SESSÃO ISOLADA LEADS #{self.lead_id}]")
        print(f" ├─ Cliente: {self.razao_social}")
        print(f" ├─ Diagnóstico Consultivo: {self.diagnostico_humano}")
        print(f" └─ Módulos Únicos Gerados: {self.modulos}")
        time.sleep(1.5)

def pulsar_engine_fabricante():
    print("============================================================")
    print("   IOTEC AGENTE ARQUITETO — MOTOR PULSANTE 24/7/365          ")
    print("============================================================")
    
    pulse_count = 0

    while True:
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id, razao_social, status_venda 
                FROM central_vendas_leads 
                WHERE status_venda IN ('PAGAMENTO_CONFIRMADO', 'EM_FABRICACAO') 
                LIMIT 5
            """)
            leads = cursor.fetchall()

            if leads:
                print(f"\n[!] {len(leads)} PEDIDOS ENCONTRADOS NA FILA! INICIANDO PROCESSAMENTO DEDICADO...")
                for lead in leads:
                    lead_id, razao, status = lead
                    relato_contexto = f"Demanda operacional para a empresa {razao}"
                    
                    arquiteto = AgenteArquitetoConsultivo(lead_id, razao, relato_contexto)
                    arquiteto.analisar_dor_isolada()
                    arquiteto.fabricar_solucao_unica()

                    cursor.execute("UPDATE central_vendas_leads SET status_venda = 'SISTEMA_ENTREGUE' WHERE id = ?", (lead_id,))
                    conn.commit()
                conn.close()
            else:
                conn.close()
                pulse_count += 1
                horario = datetime.datetime.now().strftime('%H:%M:%S')
                # Sinalizador visual de pulsação viva
                sinal = "💓 PULSANDO" if pulse_count % 2 == 0 else "🫀 PULSANDO"
                print(f"[{horario}] [{sinal}] Escutando banco iotec.db... (Aguardando novos pagamentos do gateway)", end="\r")
                time.sleep(3)

        except Exception as e:
            print(f"\n[-] Erro na pulsação do Agente: {e}")
            time.sleep(5)

if __name__ == "__main__":
    pulsar_engine_fabricante()
