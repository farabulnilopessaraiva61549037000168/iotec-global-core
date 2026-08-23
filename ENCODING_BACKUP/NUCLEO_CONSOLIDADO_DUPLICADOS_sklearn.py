import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import pandas as pd
from sklearn.ensemble import IsolationForest

# Dados de um ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rgÃƒÆ'Ã†â€™o (ex: contratos, despesas, atividades)
df = pd.read_csv("dados_governo.csv")

# Preparar modelo de detecÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de anomalias (modo sÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡bio ativado)
modelo = IsolationForest(n_estimators=100, contamination=0.05)
df['anomaly'] = modelo.fit_predict(df[['valor', 'prazo', 'quantidade']])

# Exibir contratos considerados suspeitos pelo sÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡bio
anomalias = df[df['anomaly'] == -1]
print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ALERTA DO SÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂBIO DOS SEIS CAMINHOS:")
print(anomalias[['nome_contrato', 'valor', 'responsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel']])



