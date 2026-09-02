import json, os
from datetime import datetime
PATH_LICENSES = r"C:\IOTEC\licencas_ativas.json"
def carregar_json(caminho):
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f: return json.load(f)
    return {}
def salvar_json(caminho, dados):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f: json.dump(dados, f, indent=4, ensure_ascii=False)
def validar_licenca(api_key):
    licencas = carregar_json(PATH_LICENSES)
    if api_key in licencas:
        lic = licencas[api_key]
        if lic.get("status") == "ATIVO": return True, f"Acesso liberado: {lic.get('cliente')} ({lic.get('plano')})"
    return False, "Acesso negado: Chave de API invalida ou mensalidade pendente."
licencas_base = {"IOTEC-KEY-PRO-2026": {"cliente": "Despachante Exemplo LTDA", "cnpj": "00.000.000/0001-00", "plano": "Plano Pro B2B", "status": "ATIVO", "data_ativacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
if __name__ == "__main__":
    salvar_json(PATH_LICENSES, licencas_base)
    print("🟢 [ENGINE LICENCAS] Base de licencas sincronizada com sucesso.")