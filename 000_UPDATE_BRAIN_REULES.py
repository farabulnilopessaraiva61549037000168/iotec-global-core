import sqlite3

conn = sqlite3.connect(r"C:\IOTEC\iotec_human_brain.db")
cursor = conn.cursor()

# Limpa regras antigas e reinjeta com gatilhos abrangentes sem acentuação e em minúsculas
cursor.execute("DELETE FROM matriz_atendimento")

cenarios_atualizados = [
    (
        "ABORDAGEM_INICIAL", "PRIMEIRO_CONTATO",
        "ola, bom dia, boa tarde, quem e, do que se trata, quem fala",
        "Olá! Aqui é a Camila, da IOTEC. Estou entrando em contato direto com o setor financeiro de vocês. Mapeamos um gargalo comum na emissão e liquidação de boletos na rotina da empresa e preparamos uma estrutura prática de conciliação via PIX automático para zerar essa taxa de inadimplência. Com quem eu conseguiria validar 2 minutinhos sobre isso por aqui?",
        "AGUARDAR_RESPOSTA", 45
    ),
    (
        "QUALIFICACAO", "DUVIDA_FUNCIONAMENTO",
        "como funciona, qual a proposta, o que voces fazem, me explica, me manda material, como e",
        "Perfeito! Em resumo: nossa infraestrutura se conecta ao seu sistema de vendas ou faturamento e automatiza todo o ciclo. O cliente recebe o PIX dinâmico com baixa instantânea e emissão de nota sem precisar de intervenção manual da sua equipe. Isso reduz em até 70% o tempo gasto com cobranças manuais. Vocês usam algum ERP ou emissor próprio hoje?",
        "REGISTRAR_INTERESSE", 60
    ),
    (
        "OBJECAO_PRECO", "PERGUNTA_VALOR",
        "quanto custa, qual o valor, e caro, tabela de preços, valores, qual o preço, preco, quanto fica",
        "Trabalhamos com um modelo muito enxuto para garantir retorno rápido. O investimento da licença corporativa é fixo em R$ 1.500/mês, sem taxas escondidas ou percentuais sobre o seu faturamento. Na prática, a economia em taxas de boletos e horas de equipe paga a licença logo na primeira semana. Consigo liberar o teste da estrutura para vocês ainda hoje.",
        "ENVIAR_PREPROPOSTA", 50
    ),
    (
        "OBJECAO_SEGURANCA", "CONFIRMACAO_CNPJ",
        "cnpj, empresa registrada, e seguro, qual a garantia, tem cnpj, e confiavel, empresa real",
        "Com certeza, total transparência! Nossa operação é registrada sob o CNPJ 61.549.037/0001-68 (IOTEC Enterprise). Todo o fluxo de pagamentos é processado via gateway homologado com liquidação direta na conta da sua empresa, com contrato formal e nota fiscal inclusa.",
        "ENVIAR_DADOS_INSTITUCIONAIS", 40
    ),
    (
        "FECHAMENTO", "ACEITE_PROPOSTA",
        "fechar, como pago, manda o link, manda o contrato, vamos fechar, aceito, fechar o contrato, gostei",
        "Excelente decisão! Geramos o seu termo de adesão com a ativação da licença. Você pode conferir os detalhes e liberar a entrada da sua empresa por este link seguro com chave PIX oficial do Asaas: https://iotec-global-core.onrender.com/checkout/ativa-empresa. Assim que o PIX for confirmado, nossa engenharia inicia a liberação no mesmo instante!",
        "GERAR_CHECKOUT_ASAAS", 35
    )
]

cursor.executemany('''
INSERT INTO matriz_atendimento 
(etapa, intencao_cliente, gatilhos_reconhecimento, resposta_humanizada, acao_sistema, delay_segundos)
VALUES (?, ?, ?, ?, ?, ?)
''', cenarios_atualizados)

conn.commit()
conn.close()

print("Matriz de Atendimento recarregada com sucesso e 100% calibrada!")
