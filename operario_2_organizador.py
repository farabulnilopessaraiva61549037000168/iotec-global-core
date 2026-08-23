# -*- coding: utf-8 -*-
import csv, os

CSV_PATH = r"C:\IOTEC\esteira_leads.csv"

def extrair_ddd(num): return num[2:4] if len(num) >= 4 and num.startswith("55") else "ND"

def inferir_nicho(termo):
    t = termo.lower()
    if any(k in t for k in ["imobiliaria", "moveis"]): return "IMOBILIARIO"
    if any(k in t for k in ["restaurante", "comida"]): return "GASTRONOMIA"
    if any(k in t for k in ["odont", "clinica", "estetica"]): return "SAUDE_ESTETICA"
    if any(k in t for k in ["oficina", "mecanica"]): return "AUTOMOTIVO"
    return "GERAL"

def executar_operario2():
    print("\n" + "="*70)
    print("OPERARIO 2 (ORGANIZADOR) - HIGIENIZACAO & QUALIFICACAO")
    print("="*70)
    if not os.path.exists(CSV_PATH): return
    rows = []
    with open(CSV_PATH, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader, None)
        for r in reader:
            if len(r) >= 5: rows.append(r)

    processados, novas_rows = 0, []
    for r in rows:
        data_ext, termo, nome, whatsapp, status = r[0], r[1], r[2], r[3], r[4]
        ddd = r[5] if len(r) > 5 and r[5] else extrair_ddd(whatsapp)
        nicho = r[6] if len(r) > 6 and r[6] else inferir_nicho(termo)
        if status == "NOVO":
            status = "PRONTO_PARA_CONTATO"
            processados += 1
            print(f"  [QUALIFICADO] {whatsapp} | DDD: {ddd} | Nicho: {nicho} -> PRONTO_PARA_CONTATO")
        novas_rows.append([data_ext, termo, nome, whatsapp, status, ddd, nicho])

    with open(CSV_PATH, mode='w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Data_Extracao", "Termo_Busca", "Nome_Lead", "WhatsApp_Formatado", "Status", "DDD", "Nicho"])
        writer.writerows(novas_rows)

    print(f"OPERARIO 2 CONCLUIDO: {processados} leads higienizados para abordagem.")
    print("="*70 + "\n")

if __name__ == "__main__": executar_operario2()