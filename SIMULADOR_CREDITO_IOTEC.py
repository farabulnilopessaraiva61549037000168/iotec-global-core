import sqlite3

owner = "FARABULINI LOPES SARAIVA"
cnpj = "61.549.037/0001-68"
target_mrr = 127678.57

print("==========================================================================================")
print(" 📊  IOTEC × BRADESCO PJ | SIMULADOR DE CAPACIDADE DE CRÉDITO E LIMITES                    ")
print("==========================================================================================")
print(f" [TITULAR DA OPERAÇÃO : {owner}]")
print(f" [CNPJ INSTITUCIONAL   : {cnpj}]")
print("==========================================================================================\n")

print(" ─── [ FAIXAS DE CRÉDITO E LIMITES PROJETADOS ] ──────────────────────────────────────────")
print(f"  • Faixa 1 (Abertura / Rotativo Inicial)  : R$ 15.000,00  a  R$ 50.000,00")
print(f"  • Faixa 2 (Capital de Giro / Pronampe)   : R$ 50.000,00  a  R$ 150.000,00")
print(f"  • Faixa 3 (Antecipação de Contratos 100%): R$ 100.000,00 a  R$ 300.000,00+")
print("──────────────────────────────────────────────────────────────────────────────────────────\n")

print(" ─── [ EQUAÇÃO DE GARANTIA DO BANCO ] ────────────────────────────────────────────────────")
print(f"  • Margem da Operação : 100% Líquida (Risco de Inadimplência Interna R$ 0,00)")
print(f"  • Projeção de Tração : R$ {target_mrr:,.2f} / mês em Domicílio Bancário")
print("==========================================================================================")
