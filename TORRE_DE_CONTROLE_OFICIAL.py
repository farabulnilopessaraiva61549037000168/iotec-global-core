import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC OMEGA X
# TORRE DE CONTROLE OFICIAL
# ============================================================
#
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:
# SupervisÃƒÆ'Ã†â€™o operacional do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo.
#
# RESPONSABILIDADES:
# - Monitorar oportunidades reais
# - Monitorar contratos
# - Monitorar receita
# - Monitorar produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
# - Monitorar entregas
# - Monitorar comunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
# - Monitorar rastreabilidade
# - Detectar falhas e gargalos
#
# REGRA FUNDAMENTAL:
# Nenhum dado exibido deverÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ ser simulado.
# Todos os dados devem ser provenientes de eventos
# efetivamente registrados no nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo.
#
# ============================================================

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Oportunidade:
    pass

    id: str
    instituicao: str
    setor: str

    descricao: str

    valor_estimado: float

    origem: str

    status: str

    criado_em: datetime


@dataclass
class Contrato:
    pass

    id: str

    oportunidade_id: str

    cliente: str

    valor: float

    status: str

    criado_em: datetime


@dataclass
class Projeto:
    pass

    id: str

    contrato_id: str

    responsavel: str

    status: str

    progresso: int

    criado_em: datetime


class TorreControle:
    pass

    def __init__(self):
        pass

        self.oportunidades = []

        self.contratos = []

        self.projetos = []

    # --------------------------------------------------------

    def registrar_oportunidade(self, oportunidade):
        pass

        self.oportunidades.append(oportunidade)

    # --------------------------------------------------------

    def registrar_contrato(self, contrato):
        pass

        self.contratos.append(contrato)

    # --------------------------------------------------------

    def registrar_projeto(self, projeto):
        pass

        self.projetos.append(projeto)

    # --------------------------------------------------------

    def receita_confirmada(self):
        pass

        total = 0

        for contrato in self.contratos:
            pass

            if contrato.status == "ATIVO":
                pass

                total += contrato.valor

        return total

    # --------------------------------------------------------

    def painel(self):
        pass

        print("\n")
        print("=" * 70)
        print("IOTEC - TORRE DE CONTROLE OFICIAL")
        print("=" * 70)

        print(
            f"OPORTUNIDADES........: {len(self.oportunidades)}"
        )

        print(
            f"CONTRATOS............: {len(self.contratos)}"
        )

        print(
            f"PROJETOS.............: {len(self.projetos)}"
        )

        print(
            f"RECEITA CONFIRMADA...: R$ {self.receita_confirmada():,.2f}"
        )

        print("=" * 70)


if __name__ == "__main__":
    pass

    torre = TorreControle()

    torre.painel()




