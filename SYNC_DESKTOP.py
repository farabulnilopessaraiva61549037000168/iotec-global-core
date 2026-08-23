import os

print("==================================================")
print("   IOTEC - SINCRONIZACAO COM A NUVEM 24/7        ")
print("==================================================")
print("1. Puxando atualizacoes do repositorio Git...")
os.system("git pull origin main")

print("\n2. Auditando recebimentos e eventos da nuvem...")
os.system("python 099N_SECURE_AUDIT.py")

print("\n3. Atualizando pipeline do Piloto Automatico...")
os.system("python 031_COMMERCIAL_AUTOPILOT.py")

print("\n[OK] MESA DE OPERACOES ATUALIZADA COM SUCESSO!")
print("==================================================")
