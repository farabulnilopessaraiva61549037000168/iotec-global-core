# ==============================================================================
# PROJETO: IOTEC - REFINARIA DE DADOS DE LEADS B2B
# ARQUIVO: minerador_direto.py
# DESCRIÇÃO: Processador Local de Leads B2B via CSV (Sem APIs Externas)
# ==============================================================================

import csv
import os
import re
import argparse

CAMINHO_CSV_DEFAULT = r"C:\IOTEC\leads_brutos.csv"

def limpar_telefone(telefone_raw: str) -> str:
    """Remove caracteres não numéricos do telefone."""
    if not telefone_raw:
        return ""
    return re.sub(r"\D", "", str(telefone_raw))

def validar_e_classificar_telefone(telefone_raw: str) -> dict:
    """
    Classifica e valida o telefone:
    - Móvel/WhatsApp: 10 ou 11 dígitos com corpo iniciando em 8 ou 9.
    - Fixo/PABX: Outros formatos válidos.
    """
    num = limpar_telefone(telefone_raw)
    
    if len(num) in [12, 13] and num.startswith("55"):
        num = num[2:]

    if len(num) in [10, 11]:
        ddd = num[:2]
        corpo = num[2:]
        if (len(corpo) == 9 and corpo.startswith("9")) or (len(corpo) == 8 and corpo[0] in ["8", "9"]):
            return {"valido": True, "tipo": "MÓVEL", "numero_formatado": f"55{ddd}{corpo}"}
        else:
            return {"valido": False, "tipo": "FIXO/PABX", "numero_formatado": num}
            
    return {"valido": False, "tipo": "INVÁLIDO", "numero_formatado": num}

def executar_mineracao_csv(caminho_csv: str, cliente_id: str = "Interno"):
    print("\n" + "="*70)
    print("🚀 IOTEC - REFINARIA DE DADOS (v6.0 - ENGINE LOCAL CSV)")
    print(f"👤 CLIENTE / SESSÃO: {cliente_id}")
    print(f"📁 ARQUIVO ORIGEM: {caminho_csv}")
    print("="*70 + "\n")

    if not os.path.exists(caminho_csv):
        print(f"❌ ERRO CRÍTICO: Arquivo '{caminho_csv}' não encontrado no diretório.")
        return

    ouro_validado = []
    cascalho_descartado = []

    try:
        with open(caminho_csv, mode="r", encoding="utf-8-sig") as f:
            leitor = csv.DictReader(f)
            
            for linha in leitor:
                cnpj = linha.get("cnpj", "N/A")
                nome = linha.get("razao_social", "Razão Social Não Informada")
                tel_bruto = linha.get("telefone_bruto", "")

                print(f"⛏️  LAVRA LOCAL - Processando: {nome} (CNPJ: {cnpj})...")

                # Suporta múltiplos números na mesma coluna (separados por / ou ,)
                telefones = re.split(r"[/,;]", tel_bruto)
                processado = False

                for t in telefones:
                    classificacao = validar_e_classificar_telefone(t)

                    if classificacao["valido"] and classificacao["tipo"] == "MÓVEL":
                        print(f"   💎 MINÉRIO DE OURO: {nome} | Whats: {classificacao['numero_formatado']}")
                        ouro_validado.append({
                            "cnpj": cnpj,
                            "razao_social": nome,
                            "whatsapp": classificacao["numero_formatado"]
                        })
                        processado = True
                        break
                    elif classificacao["tipo"] == "FIXO/PABX":
                        print(f"   🪨 CASCALHO ELIMINADO: {nome} | Fixo: {classificacao['numero_formatado']}")
                        cascalho_descartado.append({"cnpj": cnpj, "motivo": "Telefone Fixo/PABX"})
                        processado = True
                        break

                if not processado:
                    print(f"   ⚠️ DADOS INCOMPLETOS: {nome} não possui número móvel/válido.")

    except Exception as e:
        print(f"❌ ERRO DURANTE LEITURA DO CSV: {str(e)}")
        return

    # RELATÓRIO DA OPERAÇÃO
    print("\n" + "="*70)
    print("🎯 RELATÓRIO FINAL DE REFINO (BASE LOCAL CSV):")
    print(f"💎 Minério de Ouro (WhatsApp Móvel Validados): {len(ouro_validado)}")
    print(f"🪨 Cascalho Eliminado (Fixos / PABX Descartados): {len(cascalho_descartado)}")
    print("="*70 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IOTEC Lead Miner Local CSV Engine")
    parser.add_argument("--cliente", type=str, default="Local_User", help="ID do cliente")
    parser.add_argument("--csv", type=str, default=CAMINHO_CSV_DEFAULT, help="Caminho do CSV de origem")
    args = parser.parse_args()

    executar_mineracao_csv(caminho_csv=args.csv, cliente_id=args.cliente)