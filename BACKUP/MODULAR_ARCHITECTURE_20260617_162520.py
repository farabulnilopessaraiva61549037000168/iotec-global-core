import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  CORE SYSTEM - MODULAR ARCHITECTURE (SCAFFOLD)
# ============================================================

from dataclasses import dataclass
from typing import Dict, List
import random


# ============================================================
# 1. CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO SISTEMA
# ============================================================

@dataclass
class Config:
    population: int = 500
    seed: int = 42


# ============================================================
# 2. AGENTE (nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo comportamental)
# ============================================================

class Agent:
    def __init__(self):
        self.need = random.uniform(0, 10)
        self.preference = random.uniform(0.5, 1.5)
        self.risk = random.uniform(0.3, 1.2)

    def act(self, legal_price: float, illegal_price: float):
        legal_score = self.need - (legal_price * self.preference)
        illegal_score = self.need - (illegal_price * self.risk)

        if legal_score > illegal_score and legal_score > 0:
            return "legal"
        if illegal_score > 0:
            return "illegal"
        return "none"


# ============================================================
# 3. MOTOR DE SIMULAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O (CORE ENGINE)
# ============================================================

class CoreEngine:
    def __init__(self, config: Config):
        self.config = config
        self.agents = [Agent() for _ in range(config.population)]
        self.results = {"legal": 0, "illegal": 0, "none": 0}

    def run(self, legal_price: float, illegal_price: float):
        for a in self.agents:
            decision = a.act(legal_price, illegal_price)
            self.results[decision] += 1
        return self.results


# ============================================================
# 4. CAMADA DE MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°TRICAS (inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia do sistema)
# ============================================================

class Metrics:
    pass

    def __init__(self, results: Dict):
        self.r = results

    def total(self):
        return sum(self.r.values())

    def legal_rate(self):
        return self.r["legal"] / self.total()

    def illegal_rate(self):
        return self.r["illegal"] / self.total()

    def system_balance(self):
        return self.legal_rate() - self.illegal_rate()


# ============================================================
# 5. CAMADA DE RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO (saÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da do sistema)
# ============================================================

class Report:
    pass

    def build(self, metrics: Metrics):
        return {
            "legal_rate": round(metrics.legal_rate(), 3),
            "illegal_rate": round(metrics.illegal_rate(), 3),
            "balance": round(metrics.system_balance(), 3),
        }


# ============================================================
# 6. PIPELINE (EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO)
# ============================================================

class Pipeline:
    pass

    def __init__(self):
        self.config = Config()
        self.engine = CoreEngine(self.config)

    def execute(self, legal_price: float, illegal_price: float):
        pass

        results = self.engine.run(legal_price, illegal_price)

        metrics = Metrics(results)
        report = Report().build(metrics)

        return report


# ============================================================
# 7. EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

if __name__ == "__main__":
    pass

    system = Pipeline()

    output = system.execute(
        legal_price=5.0,
        illegal_price=3.0
    )

    print("\n=== CORE OUTPUT ===")
    for k, v in output.items():
        print(k, ":", v)


