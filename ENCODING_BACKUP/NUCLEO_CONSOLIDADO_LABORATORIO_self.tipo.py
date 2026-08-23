import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class ModuloComplexo:
    def __init__(self, nome, tipo, setor, status='ativo'):
        self.nome = nome
        self.tipo = tipo
        self.setor = setor
        self.status = status
        self.relatorios = []
        self.dependencias = []

    def validar_



