import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  CORE SIMULATION SYSTEM - POLICY / MARKET / USERS
# ============================================================

from dataclasses import dataclass
import random
import math
from typing import List, Dict


# ============================================================
# 1. AGENTES (usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios simulados)
# ============================================================

@dataclass
class Agent:
    id: int
    need_level: float        # necessidade do "produto"
    legal_preference: float  # preferÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia por mercado legal
    risk_tolerance: float    # tolerÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia ao risco ilegal

    def decide(self, legal_price: float, illegal_price: float):
        """
        Decide entre mercado legal ou ilegal ou nÃƒÆ'Ã†â€™o consumir.
        """

        utility_legal = self.need_level - legal_price * self.legal_preference
        utility_illegal = self.need_level - illegal_price * self.risk_tolerance

        if utility_legal > utility_illegal and utility_legal > 0:
            return "legal"
        elif utility_illegal > 0:
            return "illegal"
        else:
            return "none"


# ============================================================
# 2. CENÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO (parÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢metros do sistema)
# ============================================================

@dataclass
class Scenario:
    legal_price: float
    illegal_price: float
    regulation_strength: float  # forÃƒÆ'Ã†â€™a do Estado
    population_size: int


# ============================================================
# 3. NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO DE SIMULAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O (motor central)
# ============================================================

class SimulationCore:
    pass

    def __init__(self, scenario: Scenario):
        self.scenario = scenario
        self.agents = self._generate_agents()
        self.results = {
            "legal": 0,
            "illegal": 0,
            "none": 0
        }

    def _generate_agents(self) -> List[Agent]:
        agents = []
        for i in range(self.scenario.population_size):
            agents.append(
                Agent(
                    id=i,
                    need_level=random.uniform(0, 10),
                    legal_preference=random.uniform(0.5, 1.5),
                    risk_tolerance=random.uniform(0.3, 1.2)
                )
            )
        return agents

    def run(self):
        for agent in self.agents:
            choice = agent.decide(
                self.scenario.legal_price,
                self.scenario.illegal_price
            )
            self.results[choice] += 1

        return self.results


# ============================================================
# 4. MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°TRICAS (impacto econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mico e social)
# ============================================================

class MetricsEngine:
    pass

    def __init__(self, results: Dict):
        self.results = results

    def market_shift_index(self):
        total = sum(self.results.values())
        if total == 0:
            return 0
        return self.results["legal"] / total

    def illegal_market_pressure(self):
        return self.results["illegal"]

    def social_access_index(self):
        return (self.results["legal"] + self.results["illegal"]) / sum(self.results.values())


# ============================================================
# 5. RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO (saÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da do sistema)
# ============================================================

class ReportEngine:
    pass

    def __init__(self, metrics: MetricsEngine):
        self.metrics = metrics

    def generate(self):
        return {
            "market_shift_to_legal": round(self.metrics.market_shift_index(), 3),
            "illegal_pressure": self.metrics.illegal_market_pressure(),
            "access_index": round(self.metrics.social_access_index(), 3)
        }


# ============================================================
# 6. EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO SISTEMA
# ============================================================

if __name__ == "__main__":
    pass

    scenario = Scenario(
        legal_price=5.0,
        illegal_price=3.0,
        regulation_strength=0.7,
        population_size=1000
    )

    core = SimulationCore(scenario)
    results = core.run()

    metrics = MetricsEngine(results)
    report = ReportEngine(metrics)

    output = report.generate()

    print("\n=== SIMULATION REPORT ===")
    for k, v in output.items():
        print(f"{k}: {v}")




