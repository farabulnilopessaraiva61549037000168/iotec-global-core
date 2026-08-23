import json
import requests
import time

print("🔍 Iniciando Radar de CNPJs IOTEC — Sertao Central...")

# Exemplo de consulta pública de empresas ativas em Quixadá / Região (Postos/Transportes)
# O script estrutura os dados prontos para a Mesa de Operações
empresas_encontradas = [
    {
        "nome": "POSTO SERTAO CENTRAL LTDA",
        "cnpj": "12.345.678/0001-90",
        "cidade": "Quixadá",
        "telefone": "5588999001122",
        "setor": "Postos & Logística"
    },
    {
        "nome": "TRANSPORTADORA TRANSNORDESTINA REGIONAL",
        "cnpj": "98.765.432/0001-10",
        "cidade": "Quixadá",
        "telefone": "5588988112233",
        "setor": "Construção & Mineração"
    },
    {
        "nome": "LATICINIOS & LOGISTICA DO SERTAO",
        "cnpj": "45.678.910/0001-55",
        "cidade": "Quixeramobim",
        "telefone": "5588997223344",
        "setor": "Agronegócio & Laticínios"
    }
]

# Salva o arquivo de leads em formato JSON para a Mesa de Operações consumir
caminho_json = r"C:\IOTEC\leads_transnordestina.json"
with open(caminho_json, "w", encoding="utf-8") as f:
    json.dump(empresas_encontradas, f, ensure_ascii=False, indent=4)

print(f"✅ Sucesso! {len(empresas_encontradas)} empresas carregadas e vinculadas a C:\\IOTEC\\leads_transnordestina.json")