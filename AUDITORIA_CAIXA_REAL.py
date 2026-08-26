import sqlite3
import os

print("===============================================================================")
print(" 🔎 AUDITORIA DE INTEGRAÇÃO REAL — CAIXA DA FARABULINI LOPES SARAIVA")
print("===============================================================================")

# 1. Verifica se existem chaves de API reais no ambiente
asaas_key = os.getenv("ASAAS_API_KEY")
smtp_pass = os.getenv("SMTP_PASSWORD")

print(f" ├─ Chave API Asaas (Pix/Boleto Real): {'CONFIGURADA' if asaas_key else '❌ AUSENTE (Operando em MOCK)'}")
print(f" ├─ Servidor SMTP (Envio Real de E-mails): {'CONFIGURADO' if smtp_pass else '❌ AUSENTE (Apenas Print em Tela)'}")

# 2. Verifica Leads Reais vs Sintéticos no Banco
conn = sqlite3.connect("C:\\IOTEC\\iotec.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM leads_qualificados WHERE cnpj LIKE '%0001%'")
total_leads = cursor.fetchone()[0]

print(f" ├─ Total de Leads na Base Local: {total_leads}")
print(f" └─ Status do Caixa Real: ⚠️ NENHUMA TRANSAÇÃO BANCÁRIA LIQUIDADA")
print("===============================================================================")
print(" [!] CONCLUSÃO: O sistema está em MODO DE DEMONSTRAÇÃO/SIMULAÇÃO LOCAL.")
print("     Para entrar dinheiro no caixa, é obrigatório inserir as chaves das APIs reais.")
print("===============================================================================\n")
