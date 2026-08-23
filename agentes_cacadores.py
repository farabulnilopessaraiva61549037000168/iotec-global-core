# ==============================================================================
#      IOTEC - MÓDULO DE ABORDAGEM DE ALTA AUTORIDADE & DESAFIADOR (B2B)
# ==============================================================================
# CNPJ: 61.549.037/0001-68 | Responsável Técnico: Farabulini Lopes Saraiva

from core_memory import INSTITUICAO, CESTA_PRODUTOS, notificar_presidencia

# MATRIZ DE ABORDAGEM DE ELEVADO VALOR E FRICÇÃO DE ENTRADA
SCRIPTS_ABORDAGEM = {
    "LOGISTICA_BR116": {
        "perfil": "Gerentes de Frota / Transportadoras na BR-116",
        "mensagem": (
            "Identificamos instabilidade recorrente na rota de telemetria da sua frota no trecho BR-116. "
            "Não vendemos sistemas genéricos. Liberamos apenas 3 vagas de diagnóstico técnico hoje "
            "para frotas acima de 10 veículos. Acesse o portal para validar a latência do seu trecho:"
        )
    },
    "POLO_INDUSTRIAL": {
        "perfil": "Encarregados de Manutenção & TI Industrial",
        "mensagem": (
            "Seus sensores de pátio e linha de montagem podem estar operando com perda oculta de dados. "
            "A IOTEC realiza a auditoria estruturada com emissão imediata de dossiê técnico. "
            "Caso necessite de projeto customizado, a solicitação será submetida ao Gabinete da Presidência."
        )
    }
}

def disparar_abordagem_alta_autoridade(cliente, eixo, ramo, dor, ticket_sugerido, agente="Agente_Challenger"):
    """
    Executa o disparo com postura de escassez e autoridade, registrando
    a oportunidade diretamente no radar da Presidência se o ticket for de alto valor.
    """
    print(f"\n🚀 DISPARO DE ALTA AUTORIDADE -> Cliente: {cliente} [{ramo}]")
    print(f"📍 Eixo de Cobertura: {eixo}")
    print(f"💰 Ticket Proposto: R$ {ticket_sugerido:.2f}")
    
    if ticket_sugerido >= 290.00:
        print("⚡ Ticket elevado: Acionando alarme da Presidência...")
        notificar_presidencia(cliente, eixo, ramo, dor, ticket_sugerido, agente)
    else:
        print("✅ Ticket de baixo atrito: Direcionando diretamente para o Checkout Pix Instantâneo (R$ 29,90 / R$ 97,00).")

if __name__ == "__main__":
    print("=" * 65)
    print("🤖 IOTEC - SCRIPT DE TESTE DE ABORDAGEM E ESCASSEZ")
    print("=" * 65)
    disparar_abordagem_alta_autoridade(
        cliente="Expresso Logístico BR-116",
        eixo="BR-116 - Km 42 (Pacajus/CE)",
        ramo="Transportes & Frotas",
        dor="Sombra de sinal e latência no escoamento de cargas",
        ticket_sugerido=97.00
    )
    print("=" * 65)