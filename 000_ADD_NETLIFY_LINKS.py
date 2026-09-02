import sqlite3

conn = sqlite3.connect(r"C:\IOTEC\iotec_human_brain.db")
cursor = conn.cursor()

# Injeta o cenário de compra de certidões e autosserviço
cenarios_portais = [
    (
        "AUTOSSERVICO_CERTIDOES", "COMPRA_DIRETA_CERTIDAO",
        "certidao, certidoes, comprar certidao, portal, site, emitir certidao, servicos",
        "Você pode solicitar e emitir suas certidões e serviços diretamente pelo nosso Portal Institucional de Autoatendimento: https://sparkling-mooncake-a4f11d.netlify.app/ . O processo é 100% automatizado e a emissão é liberada logo após a confirmação do PIX!",
        "DIRECIONAR_PORTAL_NETLIFY", 30
    ),
    (
        "FECHAMENTO_PORTAL", "LINK_DIRETO_OPERACAO",
        "link do site, onde compro, acessar plataforma, central de operacoes",
        "Perfeito! Você pode acessar nossa Central de Operações e concluir a contratação diretamente por este link seguro: https://deft-choux-097d84.netlify.app/ . Qualquer dúvida durante a navegação, estou à disposição por aqui!",
        "DIRECIONAR_CENTRAL_NETLIFY", 25
    )
]

cursor.executemany('''
INSERT INTO matriz_atendimento 
(etapa, intencao_cliente, gatilhos_reconhecimento, resposta_humanizada, acao_sistema, delay_segundos)
VALUES (?, ?, ?, ?, ?, ?)
''', cenarios_portais)

conn.commit()
conn.close()

print("[OK] Links dos Portais Netlify integrados à inteligência da Agente Camila!")
