import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  CORE STRESS TEST SYSTEM (v2)
# Monte Carlo + Scenario Sweep + Robustness Analysis
# ============================================================

import random
from dataclasses import dataclass
from typing import Dict, List


# ============================================================
# 1. AGENTE (comportamento mais sensÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel a variaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o)
# ============================================================

class Agent:
    def __init__(self):
        self.need = random.uniform(0, 10)
        self.preference_legal = random.uniform(0.3, 1.7)
        self.risk_sensitivity = random.uniform(0.2, 1.5)

    def decide(self, legal_price, illegal_price):
        u_legal = self.need - (legal_price * self.preference_legal)
        u_illegal = self.need - (illegal_price * self.risk_sensitivity)

        if u_legal > u_illegal and u_legal > 0:
            return "legal"
        elif u_illegal > 0:
            return "illegal"
        return "none"


# ============================================================
# 2. CENÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO DINÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡MICO (stress variÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel)
# ============================================================

@dataclass
class Scenario:
    legal_price: float
    illegal_price: float
    regulation: float
    population: int


# ============================================================
# 3. CORE ENGINE
# ============================================================

class CoreEngine:
    pass

    def __init__(self, scenario: Scenario):
        self.scenario = scenario
        self.agents = [Agent() for _ in range(scenario.population)]
        self.results = {"legal": 0, "illegal": 0, "none": 0}

    def run(self):
        for a in self.agents:
            decision = a.decide(
                self.scenario.legal_price,
                self.scenario.illegal_price
            )
            self.results[decision] += 1
        return self.results


# ============================================================
# 4. STRESS TESTER (o ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"olho de tamberaÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â real)
# ============================================================

class StressTester:
    pass

    def __init__(self, runs=50):
        self.runs = runs
        self.snapshots = []

    def random_scenario(self):
        return Scenario(
            legal_price=random.uniform(3, 10),
            illegal_price=random.uniform(2, 8),
            regulation=random.uniform(0.1, 1.0),
            population=random.randint(200, 1000)
        )

    def run_test(self):
        for i in range(self.runs):
            scenario = self.random_scenario()
            engine = CoreEngine(scenario)
            result = engine.run()

            total = sum(result.values())
            snapshot = {
                "run": i,
                "legal_ratio": result["legal"] / total,
                "illegal_ratio": result["illegal"] / total,
                "none_ratio": result["none"] / total,
            }

            self.snapshots.append(snapshot)

        return self.snapshots


# ============================================================
# 5. ANALYTICS ENGINE (musculatura do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo)
# ============================================================

class Analytics:
    pass

    def __init__(self, snapshots: List[Dict]):
        self.data = snapshots

    def average_legal(self):
        return sum(d["legal_ratio"] for d in self.data) / len(self.data)

    def volatility(self):
        avg = self.average_legal()
        return sum(abs(d["legal_ratio"] - avg) for d in self.data) / len(self.data)

    def robustness_score(self):
        """
        quanto MENOS variaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, mais robusto o sistema
        """
        return 1 / (1 + self.volatility())


# ============================================================
# 6. EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO STRESS TEST
# ============================================================

if __name__ == "__main__":
    pass

    tester = StressTester(runs=100)
    results = tester.run_test()

    analytics = Analytics(results)

    print("\n=== CORE STRESS TEST REPORT ===")
    print(f"Average Legal Adoption: {analytics.average_legal():.3f}")
    print(f"Volatility: {analytics.volatility():.3f}")
    print(f"Robustness Score: {analytics.robustness_score():.3f}")




