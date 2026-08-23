from pathlib import Path
import shutil
import ast
from datetime import datetime

ARQUIVO = Path(r"C:\IOTEC\000_IOTEC_CORE.py")

BACKUP = ARQUIVO.with_suffix(".backup.py")

NOVO = ARQUIVO.parent / "000_IOTEC_CORE_V2.py"

print("="*70)
print("IOTEC CORE MIGRATOR")
print("="*70)

if not ARQUIVO.exists():
    raise FileNotFoundError(ARQUIVO)

print("Criando Backup...")

shutil.copy2(ARQUIVO, BACKUP)

print("OK")

codigo = ARQUIVO.read_text(encoding="utf-8")

print("Validando Sintaxe...")

ast.parse(codigo)

print("Sintaxe OK")

cabecalho = f'''
"""
==========================================================
IOTEC CORE V2
Gerado automaticamente

Data:

{datetime.now()}

==========================================================
"""
'''

NOVO.write_text(cabecalho + "\n" + codigo, encoding="utf-8")

print()

print("Novo Kernel criado:")

print(NOVO)

print()

print("Backup:")

print(BACKUP)

print()

print("MigraÃ§Ã£o concluÃ­da.")

