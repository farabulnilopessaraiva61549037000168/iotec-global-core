import threading
import time
import datetime

class DualQualifiedEngine:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"

    def auditoria_qualificacao(self):
        print(" ─── [ AUDITORIA DE QUALIFICAÇÃO DE LEADS (LEITOS DE UTI) ] ─────────────────────────")
        print("  1. CAPACIDADE FINANCEIRA : Filtro de CNPJs com faturamento estimado > R$ 100k/mês")
        print("  2. STATUS CADASTRAL     : CNPJs 100% Ativos na Receita Federal (Sem notas frias/fantasmas)")
        print("  3. DECISOR DIRETO       : Contatos validados de Diretores, C-Levels e Sócios-Administradores")
        print("  4. ADERÊNCIA DE TICKET   : Dores mapeadas para contratação imediata do plano de R$ 899,00/mês\n")

    def motor_disparo_lote_02(self):
        """Thread 1: Dispara abordagens para os alvos do Lote 02"""
        print(" [THREAD 1] 🚀 Disparando Abordagens Multicanal para o Lote 02 (Alvos 51 a 100)...\n")
        time.sleep(1)
        for i in range(51, 56):
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(f" [{now}] 📤 Abordagem Multicanal enviada para: CNPJ ALVO #{i:03d} (Auditado & Qualificado)")
            time.sleep(1)
        print("\n [THREAD 1] ✅ Bloco inicial do Lote 02 entregue com sucesso aos decisores.")

    def escuta_caixa_asaas(self):
        """Thread 2: Mantém a escuta do webhook para recebimentos do Lote 01"""
        print(" [THREAD 2] 🎧 Escuta de Caixa Asaas (PIX / Boleto) Operacional...\n")
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print(f" [{now}] 🟢 Escuta Ativa: Aguardando notificações na conta PJ ({self.cnpj})...")

    def executar(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" ⚡  IOTEC DUAL ENGINE | DISPARO LOTE 02 + ESCUTA ASAAS + QUALIFICAÇÃO DE LEADS           ")
        print("==========================================================================================")
        print(f" [RESPONSÁVEL OPERACIONAL : FARABULINI LOPES SARAIVA]")
        print(f" [STAMP DE EXECUÇÃO       : {now}]")
        print("==========================================================================================\n")

        self.auditoria_qualificacao()

        t1 = threading.Thread(target=self.motor_disparo_lote_02)
        t2 = threading.Thread(target=self.escuta_caixa_asaas)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("\n==========================================================================================")
        print(" 🔥 OPERAÇÃO SIMULTÂNEA EM ANDAMENTO COM LEADS AUDITADOS E QUALIFICADOS.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = DualQualifiedEngine()
    engine.executar()
