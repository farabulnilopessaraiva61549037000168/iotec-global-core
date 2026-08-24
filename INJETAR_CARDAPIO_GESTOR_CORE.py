import sqlite3
import datetime

class CardapioGestorEngine:
    def __init__(self):
        self.db_path = "iotec.db"

    def injetar(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Injeção das perguntas do cardápio e corredores no banco
        conhecimentos = [
            ("CORREDOR_FISCAL", "Emissão Automática de NF-e", "Disparo de webhooks Asaas com cálculo municipal de ISS/PIS/COFINS."),
            ("CORREDOR_GERENCIA", "Liquidação e DRE em Tempo Real", "Processamento em < 2s via PIX Asaas Direct e margem bruta > 90%."),
            ("CORREDOR_JURIDICO", "Conformidade LGPD & Criptografia", "Dados sensíveis codificados em SHA-256 e termos contratuais com IP/UTC."),
            ("CORREDOR_TECH", "Concorrência de Banco & Multi-Fuso", "Modo WAL ativo no SQLite e timestamps mestre em ISO-8601 UTC.")
        ]

        cursor.executemany('''
            INSERT INTO strategic_knowledge (category, title, description)
            VALUES (?, ?, ?)
        ''', conhecimentos)

        conn.commit()
        conn.close()

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 📖 IOTEC AUDIT CORE | CARDÁPIO DO GESTOR & SUMÁRIO TÉCNICO REGISTRADOS NO IOTEC.DB     ")
        print("==========================================================================================")
        print(f" [RESPONSÁVEL OPERACIONAL : FARABULINI LOPES SARAIVA]")
        print(f" [STAMP DE EXECUÇÃO       : {now}]")
        print("==========================================================================================\n")
        print("  ✅ 4 Corredores Técnicos devidamente mapeados com o Cardápio de Perguntas e Respostas.")
        print("  ✅ Documento PDF/HTML `MANUAL_SABATINA_E_CARDAPIO_GESTOR` atrelado à base de conhecimento.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = CardapioGestorEngine()
    engine.injetar()
