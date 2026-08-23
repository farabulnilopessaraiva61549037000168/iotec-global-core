from core_memory import CESTA_PRODUTOS, INSTITUICAO

print("=" * 65)
print(f"   📋 IOTEC - AUDITORIA DE CAPACIDADE DE ENTREGA OPERACIONAL")
print("=" * 65)
print(f"Empresa: {INSTITUICAO['nome_fantasia']} | CNPJ: {INSTITUICAO['cnpj']}\n")

for chave, prod in CESTA_PRODUTOS.items():
    print(f"📦 Produto: {prod['nome']}")
    print(f"   💰 Valor: R$ {prod['valor_padrao']:.2f}")
    print(f"   🛠️ Escopo entregável: {prod['bastidores']}")
    print(f"   Status de Entrega: AUTOMÁTICO VIA PLATAFORMA NUVEM")
    print("-" * 65)

print("\n💡 DIRETRIZ COMERCIAL: Focar disparos nos itens de ticket R$ 29,90 e R$ 97,00")
print("   para gerar volume rápido de conversão e validar o caixa.")
print("=" * 65)