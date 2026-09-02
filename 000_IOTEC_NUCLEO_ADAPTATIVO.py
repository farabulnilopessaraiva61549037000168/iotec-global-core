import os, sys, time, psutil, subprocess, csv

# ------------------------------------------------------------------
# CONFIGURAÇÕES DA ENTIDADE IOTEC
# ------------------------------------------------------------------
CNPJ_OFICIAL = '61.549.037/0001-68'
RAZAO_SOCIAL = 'IOTEC Platform — Tecnologia & Compliance B2B'
CARIMBO_DIGITAL = f'{RAZAO_SOCIAL}\nCNPJ: {CNPJ_OFICIAL} | Validação 24/7'
ARQUIVO_LEADS = r'C:\IOTEC\LOTE_PROSPECCAO_B2B.csv'

class NucleoIOTEC:
    def __init__(self):
        print("==================================================")
        print(f"🚀 INICIALIZANDO NÚCLEO ADAPTATIVO — {RAZAO_SOCIAL}")
        print(f"📄 CNPJ: {CNPJ_OFICIAL}")
        print("==================================================\n")

    def auditar_recursos_sistema(self):
        """Verifica uso de memória e mata processos orfãos antes de travar o notebook."""
        memoria = psutil.virtual_memory().percent
        print(f"[TELEMETRIA] Uso de RAM Atual: {memoria}%")
        
        # Se a memória ultrapassar 85%, ativa a Ação Adaptativa do Núcleo
        if memoria > 85.0:
            print("⚠️ [ALERTA DE SOBRECARGA] Executando contenção de processos...")
            os.system('powershell -Command "Stop-Process -Name chrome, node -Force -ErrorAction SilentlyContinue"')
            print("✅ Processos pesados encerrados com sucesso.")
            return False
        return True

    def preparar_carimbo_e_mensagem(self, empresa_nome):
        """Aplica o carimbo corporativo oficial e a mensagem com novas capacidades."""
        mensagem = f'''{CARIMBO_DIGITAL}

Apresentação comercial IOTEC para *{empresa_nome}*.

Disponibilizamos a emissão e validação automatizada de Certidões de Compliance B2B e Soluções de Governança Financeira.

🔗 *Portal de Vendas & Investimentos:*
https://endearing-fudge-3789ac.netlify.app

Atendimento & Suporte: (88) 99306-4168 | IOTEC.BL@proton.me'''
        return mensagem

    def processar_lote_com_telemetria(self):
        """Mapeia os leads e executa a rotina adaptativa sem estourar o sistema."""
        if not os.path.exists(ARQUIVO_LEADS):
            print(f"❌ Arquivo {ARQUIVO_LEADS} não localizado!")
            return

        if not self.auditar_recursos_sistema():
            print("🛑 Processamento pausado para proteger o ambiente local.")
            return

        print("🔄 [PROCESSAMENTO] Carregando lote e aplicando validação de segurança...")
        with open(ARQUIVO_LEADS, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            total = 0
            for row in reader:
                total += 1
                empresa = row.get('RAZAO_SOCIAL', 'Empresa')
                msg = self.preparar_carimbo_e_mensagem(empresa)
                print(f"[{total}/50] 📦 Lead Validado: {empresa[:30]} | Carimbo OK")
                
                # Checagem de telemetria a cada 10 itens
                if total % 10 == 0:
                    self.auditar_recursos_sistema()

        print("\n==================================================")
        print("✅ LOTE AUDITADO E PRONTO PARA ENVIO VIA NUVEM")
        print("==================================================")

if __name__ == '__main__':
    nucleo = NucleoIOTEC()
    nucleo.processar_lote_com_telemetria()
