import os
import shutil
import glob

print("=" * 65)
print("   IOTEC PLATFORM - CONSOLIDAÇÃO DO ACERVO DE INTERFACES")
print("=" * 65)

base_dir = r"C:\IOTEC"
acervo_dir = os.path.join(base_dir, "acervo")
os.makedirs(acervo_dir, exist_ok=True)

user_profile = os.environ.get("USERPROFILE")
downloads_dir = os.path.join(user_profile, "Downloads")

# Lista de arquivos prioritários identificados para resgate imediato
priority_files = [
    "TORRE DE CONTROLE IOTEC.htm",
    "IOTEC EXECUTIVE DASHBOARD.htm",
    "IOTEC OMEGA CORE.htm",
    "REGULUS - Painel Operacional Master.htm",
    "regulus cockpit.htm",
    "ShopTec — Tecnologia e Inovação Digital · IOTEC BL.htm",
    "🎯 Sistema de Rotas de Compradores.htm",
    "💎 Catálogo Premium - Sistema Omega.htm"
]

copied_count = 0
for file in priority_files:
    # Busca o arquivo em Downloads
    matches = glob.glob(os.path.join(downloads_dir, "**", file), recursive=True)
    if not matches:
        matches = glob.glob(os.path.join(downloads_dir, file))
        
    if matches:
        src = matches[0]
        dst = os.path.join(acervo_dir, os.path.basename(src))
        try:
            shutil.copy2(src, dst)
            print(f"✅ Resgatado: [{os.path.basename(src)}]")
            copied_count += 1
        except Exception as e:
            print(f"⚠️ Erro ao copiar {file}: {e}")

print(f"\n>>> Total de interfaces principais resgatadas para C:\\IOTEC\\acervo: {copied_count}")
print("=" * 65)
