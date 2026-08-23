import getpass
import re

print("=" * 55)
print("   IOTEC SECURITY - CREDENCIAMENTO DE CHAVE / SENHA")
print("=" * 55)

# 1. Entrada oculta da Chave / Secret
while True:
    key_input = getpass.getpass("\n[1/2] Digite sua Chave/Token/Senha (oculto): ")
    if not key_input.strip():
        print("❌ A chave não pode ser vazia. Tente novamente.")
        continue
        
    confirm_input = getpass.getpass("[2/2] Confirme a Chave/Token/Senha (oculto): ")
    
    if key_input == confirm_input:
        print("\n✅ Validação confirmada! As chaves coincidem.")
        break
    else:
        print("\n❌ As chaves digitadas não coincidem. Tente novamente.")

# 2. Atualização segura no arquivo .env
env_path = r"C:\IOTEC\.env"

try:
    with open(env_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Substitui a chave genérica pela chave credenciada
    new_content = content.replace("SUA_CHAVE_PIX_REAL_AQUI", key_input)
    new_content = new_content.replace("SUA_CHAVE_AQUI", key_input)
    
    # Atualiza o modo para produção
    new_content = new_content.replace("PAYMENT_ENV=sandbox", "PAYMENT_ENV=production")

    with open(env_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("\n" + "=" * 55)
    print("🔒 CREDENCIAMENTO CONCLUÍDO COM SUCESSO!")
    print("   Os dados foram gravados diretamente no C:\\IOTEC\\.env")
    print("   O campo permanece disponível para alteração futura via script.")
    print("=" * 55)

except Exception as e:
    print(f"\n❌ Erro ao atualizar o arquivo .env: {e}")
