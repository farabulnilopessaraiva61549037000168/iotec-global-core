import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
// ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Âµ CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDIGO MATRIZ - COMPLEXO DIGITAL GLOBAL
// ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Central Operacional - VersÃƒÆ'Ã†â€™o 1.0
// ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ FormulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o EstratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gica, Financeira, Operacional e de Escalabilidade Global

INICIAR_PROJETO() {
    DEFINIR_SEDE("Estados Unidos", "Modelo Digital", "Registro via Stripe Atlas ou Doola");
    DEFINIR_MOEDA_PRINCIPAL("USD");
    DEFINIR_OPERACAO("100% Digital", "Global", "Multinacional", "EscalÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel");

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Setores
    SETORES = ["AdministraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", "Financeiro", "Tecnologia", "Marketing", "OperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes", "JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico"];

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Modelagem Financeira
    CUSTO_FIXO_MENSAL = 3800; // em USD
    CUSTO_VARIAVEL_MENSAL = 0.22 * FATURAMENTO_BRUTO;
    IMPOSTOS_TOTAIS = 0.12 * FATURAMENTO_BRUTO; // EUA + Taxas internacionais

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â½Ãƒâ€šÃ‚Â¯ ProjeÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de Receita
    CLIENTES_MENSAL = PROJETAR_CLIENTES_MES(INICIO=120, CRESCIMENTO=18%);
    TICKET_MEDIO = 1550; // em USD

    FATURAMENTO_BRUTO = CLIENTES_MENSAL * TICKET_MEDIO;
    LUCRO_BRUTO = FATURAMENTO_BRUTO - (CUSTO_FIXO_MENSAL + CUSTO_VARIAVEL_MENSAL + IMPOSTOS_TOTAIS);

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€¦Ã‚Â½ Lucro lÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­quido apÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³s reservas
    RESERVA_TECNOLOGIA = 0.08 * FATURAMENTO_BRUTO;
    RESERVA_MARKETING = 0.06 * FATURAMENTO_BRUTO;
    RESERVA_EXPANSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O = 0.05 * FATURAMENTO_BRUTO;

    LUCRO_LIQUIDO = LUCRO_BRUTO - (RESERVA_TECNOLOGIA + RESERVA_MARKETING + RESERVA_EXPANSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O);

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ Escalabilidade
    if (CLIENTES_MENSAL >= 300) {
        ATIVAR_ESCALONAMENTO();
    }

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â ExpansÃƒÆ'Ã†â€™o Global
    PAISES_ALVO = ["Brasil", "Portugal", "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Ândia", "JapÃƒÆ'Ã†â€™o", "Singapura", "Chile", "ColÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mbia", "MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©xico", "CanadÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡"];
    ANALISAR_DEMANDA_POR_PAIS(PAISES_ALVO);
    DEFINIR_PRIORIDADE(PAISES_ALVO, BASEADO_EM=["Margem de Lucro", "Baixa Burocracia", "Alta Demanda"]);

    // ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Matriz de Riscos
    ANALISAR_RISCOS(["JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico", "Financeiro", "TecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gico", "Cultural", "Operacional"]);
    ATIVAR_CONTINGENCIAS();

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Sistema AutÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´nomo
    SISTEMA_AUTOMATICO = true;
    SISTEMA_BACKUP = true;
    SISTEMA_DESCONEXAO = "Independente da internet global";

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â½Ãƒâ€šÃ‚Â¨ Branding
    IMAGEM_MERCADO = "Empresa Premium, Sede nos EUA, Alta Credibilidade";

    // ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒâ€šÃ‚ÂºÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Painel Visual
    ATIVAR_PAINEL([
        "Mapa de Faturamento por PaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­s",
        "GrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ficos Crescimento Mensal",
        "Alertas de Risco",
        "Checklist de OperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"
    ]);

    // ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Encerramento de Loop Mensal
    RELATORIO_MENSAL(FATURAMENTO_BRUTO, LUCRO_LIQUIDO, CLIENTES_MENSAL, STATUS_EXPANSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O, STATUS_RISCO);
}

// ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes Complementares
PROJETAR_CLIENTES_MES(INICIO, CRESCIMENTO) {
    INICIAR_COMPLEXO_DIGITAL
{
    // IDENTIDADE CORPORATIVA
    DEFINIR_SEDE = "Estados Unidos"
    MODELO_EMPRESA = "100% DIGITAL"
    OPERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O_GLOBAL = TRUE
    REGIÃƒÆ'Ã†â€™ES_FOCO = ["AmÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rica Latina", "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âsia Maior", "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âsia Menor", "Europa Sul", "Portugal", "Brasil", "Mercados Subexplorados"]

    // ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GIA COMERCIAL
    MODELO_NEGÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œCIO = "MULTISERVIÃƒÆ'Ã†â€™OS EM TORRES DIGITAIS"
    DIFERENCIAL_COMPETITIVO = ["Empresa sediada nos EUA", "Imagem premium internacional", "Baixo custo operacional", "Alta credibilidade", "ServiÃƒÆ'Ã†â€™os automatizados"]
    POLÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICA_PREÃƒÆ'Ã†â€™OS = "PreÃƒÆ'Ã†â€™o competitivo, faturamento em dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lar, pagamento global"
    RECEBIMENTO = "Moeda forte convertida para reais"

    // ESTRUTURA OPERACIONAL
    SETORES_ATIVOS = [
        "Arquitetura Digital e Engenharia",
        "Desenvolvimento de Projetos EcolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gicos e SustentÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡veis",
        "Consultorias Empresariais e Documentais",
        "Planejamento Urbano Digital",
        "ServiÃƒÆ'Ã†â€™os JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dicos Documentais Internacionais",
        "AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lises EstratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicas e InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Empresarial"
    ]
    SISTEMA_FUNCIONAMENTO = "AutomÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico, Independente, EscalÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel, Nuvem Privada + Backup Local"

    // MODELO DE ATENDIMENTO
    MODELO_RECEPÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O = "SalÃƒÆ'Ã†â€™o Virtual com GuichÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs SimultÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢neos"
    ATENDIMENTO = "AssÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ncrono + SÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ncrono | Multicanal | Suporte Global"
    EXPERIÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA_CLIENTE = "PadrÃƒÆ'Ã†â€™o hotel de luxo digital"

    // FINANCEIRO E PROJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
    FATURAMENTO_OTIMISTA_MENSAL = 179450.55 // em dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lar
    FATURAMENTO_CONSERVADOR_MENSAL = 105000.00 // estimativa segura
    FATURAMENTO_ANUAL = FATURAMENTO_MENSAL * 12
    LUCRO_BRUTO = FATURAMENTO - CUSTOS_OPERACIONAIS
    LUCRO_LIQUIDO = LUCRO_BRUTO - IMPOSTOS - TERCEIRIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES

    // EXPANSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O E ESCALABILIDADE
    MONITORAMENTO_DEMANDA_MUNDIAL()
    PRIORIZAR_REGIÃƒÆ'Ã†â€™ES_COM_MAIOR_LUCRO()
    ADAPTAR_SERVIÃƒÆ'Ã†â€™OS_POR_CULTURA_E_MERCADO()

    // PAINÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°IS E MONITORAMENTO
    GERAR_PAINEL {
        MAPAS_INTERATIVOS_POR_PAÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂS
        GRÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂFICOS_DE_DEMANDA
        GRÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂFICOS_DE_FATURAMENTO
        DASHBOARD_FINANCEIRO
        ALERTAS_ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICOS
        LEMBRETES_OPERACIONAIS
    }

    // PROTOCOLO DE ESCALABILIDADE
    SE (DEMANDA >= 80% DA_CAPACIDADE) {
        ATIVAR_EXPANSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O_AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICA
        REPLICAR_INFRAESTRUTURA_NUVEM
        ABRIR_NOVOS_GUICHES_VIRTUAIS
    }

    // SEGURANÃƒÆ'Ã†â€™A E CONTINGÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA
    ATIVAR_BACKUP_AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICO
    ATIVAR_CONTINGÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA_LOCAL_SE_OFFLINE
    PROTEGER_DADOS_COM_CIFRA_MILITAR

    // VALORES E CULTURA CORPORATIVA
    VALORES = ["ExcelÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia", "Credibilidade", "Sustentabilidade", "AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", "InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Aplicada"]
    FOCO = ["Desbancar concorrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia local com preÃƒÆ'Ã†â€™o justo + alta qualidade"]

    // EXECUTAR
    INICIAR_OPERACAO_GERAL()
}



