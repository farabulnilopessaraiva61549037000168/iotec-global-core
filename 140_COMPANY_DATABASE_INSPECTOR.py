import json

with open("IOTEC_COMPANY_DATABASE.json","r",encoding="utf-8") as f:
    data=json.load(f)

print("="*80)
print("INSPEÃƒâ€¡ÃƒÆ'O DO BANCO")
print("="*80)
print()

print("Total:",len(data))
print()

print("PRIMEIRO REGISTRO")
print()

print(json.dumps(data[0],indent=4,ensure_ascii=False))

