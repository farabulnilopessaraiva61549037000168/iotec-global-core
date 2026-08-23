import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ Painel do Modo SÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡bio Supremo ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Sistema de Defesa e Sabedoria

import pandas as pd import matplotlib.pyplot as plt import seaborn as sns from sklearn.ensemble import IsolationForest from datetime import datetime

=== 1. Carregamento dos dados do "mundo real" ===

df = pd.read_csv("dados_governo.csv") # Substituir pelo caminho real do CSV

=== 2. Ativar o "Modo SÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡bio dos Seis Caminhos" ===

modelo = IsolationForest(n_estimators=150, contamination=0.05, random_state=42) df['anomaly'] = modelo.fit_predict(df[['valor', 'prazo', 'quantidade']])

=== 3. Criar o Painel de VisÃƒÆ'Ã†â€™o ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°tica ===

print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â½ VISÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO SÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂBIO ATIVADA ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ANÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLISE DE FLUXOS E DISTORÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES")

anomalias = df[df['anomaly'] == -1] if len(anomalias) == 0: print("Tudo estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ equilibrado no chakra do sistema.") else: print(f"{len(anomalias)} desvios encontrados nos contratos:") print(anomalias[['nome_contrato', 'valor', 'prazo', 'responsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel']])

=== 4. Criar o Mapa Visual ===

sns.set(style="whitegrid") plt.figure(figsize=(12,6)) sns.scatterplot(data=df, x="prazo", y="valor", hue="anomaly", palette={1: "green", -1: "red"}) plt.title("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ VisÃƒÆ'Ã†â€™o do SÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡bio ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°tica de Contratos") plt.xlabel("Prazo do Contrato (dias)") plt.ylabel("Valor do Contrato (R$)") plt.legend(title="Status") plt.tight_layout() plt.show()

=== 5. EmissÃƒÆ'Ã†â€™o de RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio ===

hoje = datetime.now().strftime('%Y-%m-%d') relatorio = f"relatorio_sabio_{hoje}.csv" anomalias.to_csv(rel




