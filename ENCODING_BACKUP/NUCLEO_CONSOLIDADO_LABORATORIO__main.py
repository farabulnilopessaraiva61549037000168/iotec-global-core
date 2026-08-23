import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# main.py

from modulo_consciencia import Consciencia
from modulo_varredura import Varredura
from modulo_acao import Executor
from modulo_relatorios import Relatorio

# Inicializando o sistema
cons = Consciencia()
print(cons.saudacao())

# Fazendo varredura
scanner = Varredura("./")
arquivos = scanner.diagnostico()

# Executando aÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
executor = Executor()
acao = executor.executar("Organizar pastas internas")

# Gerando relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio
relatorio = Relatorio()
relatorio.adicionar_item(f"Arquivos encontrados: {len(arquivos)}")
relatorio.adicionar_item(acao)
print(relatorio.gerar())

print("[Sistema Vivo] Ciclo concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do.")



