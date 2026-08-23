import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import numpy as np
import networkx as nx
from scipy.optimize import minimize
from sklearn.cluster import KMeans

# Criando um grafo representando o mercado nacional
G = nx.erdos_renyi_graph(n=1000, p=0.05)  # SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de conexÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes no mercado

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de crescimento exponencial para simular a expansÃƒÆ'Ã†â€™o do serviÃƒÆ'Ã†â€™o
def growth_model(t, alpha, beta):
    return alpha * np.exp(beta * t)

# OtimizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para maximizar arrecadaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ativa e passiva
def revenue_optimization(x):
    return -1 * (np.sum(np.log(1 + x)) + np.sum(np.sin(x)))  # Maximiza retorno financeiro

# Encontrando pontos estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicos para ataque no mercado
kmeans = KMeans(n_clusters=10)
nodes = np.array(list(G.nodes()))
kmeans.fit(nodes.reshape(-1, 1))
key_targets = kmeans.cluster_centers_

# Aplicando otimizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
result = minimize(revenue_optimization, np.random.rand(len(nodes)), method='BFGS')

print("Pontos estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicos para inserÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o no mercado:", key_targets)
print("ArrecadaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o esperada otimizada:", -result.fun)



