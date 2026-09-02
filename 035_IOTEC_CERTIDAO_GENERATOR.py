import sqlite3
import datetime

def gerar_certidao(lead_id):
    conn = sqlite3.connect(r'C:\IOTEC\iotec_kernel.db')
    c = conn.cursor()
    c.execute("SELECT empresa, pais_codigo, score_match FROM iotec_corporate_leads WHERE id = ?", (lead_id,))
    data = c.fetchone()
    conn.close()
    
    if data:
        print(f"--- CERTIDÃO DE QUALIFICAÇÃO IOTEC ---")
        print(f"EMPRESA: {data[0]}")
        print(f"PAÍS: {data[1]}")
        print(f"SCORE MATCH: {data[2]}%")
        print(f"AUTENTICAÇÃO: CNPJ 61.549.037/0001-68")
        print(f"DATA DE EMISSÃO: {datetime.datetime.now()}")
    else:
        print("Lead não localizado para emissão de certidão.")

if __name__ == '__main__':
    gerar_certidao(1)
