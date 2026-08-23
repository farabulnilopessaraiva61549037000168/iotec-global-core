import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations
import argparse
import importlib.util
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR = Path(__file__).resolve().parents[2]
CONFIG_PATH = BASE_DIR / "CONFIG" / "nucleus_config.json"
MODULES_DIR = BASE_DIR / "MODULES"

sys.path.insert(0, str(MODULES_DIR))
from common.helpers import (
    append_log,
    compress_complexity_logarithmically,
    ensure_dir,
    env_info,
    load_json,
    reliability_score,
    save_json,
    write_snapshot,
    now_iso,
)


@dataclass
class CommandEnvelope:
    plate: str
    objective: str
    risk: float
    confidence_inputs: Dict[str, float]
    metadata: Dict[str, Any] = field(default_factory=dict)

    def score(self) -> float:
        return reliability_score(self.confidence_inputs)


class AtmosphereFilter:
    def __init__(self, config: Dict[str, Any], log_path: Path):
        self.config = config
        self.log_path = log_path

    def validate(self, envelope: CommandEnvelope) -> Dict[str, Any]:
        score = envelope.score()
        reliability_cfg = self.config.get("reliability", {})
        minimum_score = float(reliability_cfg.get("minimum_score", 0.72))

        reasons: List[str] = []
        blocked = False

        if score < minimum_score:
            blocked = True
            reasons.append(
                f"Confiabilidade insuficiente: {score:.4f} < {minimum_score:.4f}"
            )

        if self.config.get("integration", {}).get("block_on_unknown_mapping", True):
            if envelope.plate == "integrate" and not envelope.metadata.get("mapping_defined", False):
                blocked = True
                reasons.append("IntegraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o sem mapeamento definido.")

        if self.config.get("integration", {}).get("block_on_missing_contract", True):
            if envelope.plate == "integrate" and not envelope.metadata.get("contract_defined", False):
                blocked = True
                reasons.append("IntegraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o sem contrato de dados definido.")

        if self.config.get("reliability", {}).get("block_on_untrusted_formula", True):
            if envelope.metadata.get("formula_trusted", True) is False:
                blocked = True
                reasons.append("FÃƒÆ'Ã‚Â³rmula rejeitada por falta de respaldo.")

        if blocked:
            append_log(self.log_path, "BLOCK", f"[{envelope.plate}] {envelope.objective} | {'; '.join(reasons)}")
        else:
            append_log(self.log_path, "PASS", f"[{envelope.plate}] {envelope.objective} | score={score:.4f}")

        return {
            "blocked": blocked,
            "score": score,
            "reasons": reasons
        }


class GravityController:
    def __init__(self, log_path: Path):
        self.log_path = log_path

    def pull_to_core(self, plate: str, result: Dict[str, Any]) -> Dict[str, Any]:
        append_log(self.log_path, "RETURN", f"Placa '{plate}' retornou ao nÃƒÆ'Ã‚Âºcleo.")
        return {
            "returned_to_core": True,
            "plate": plate,
            "result": result
        }


class PlateExecutor:
    def __init__(self, base_dir: Path, log_path: Path):
        self.base_dir = base_dir
        self.log_path = log_path
        self.results_dir = ensure_dir(base_dir / "STATE" / "results")
        self.integration_dir = ensure_dir(base_dir / "STATE" / "integration")
        self.commercial_dir = ensure_dir(base_dir / "STATE" / "commercial")

    def execute(self, envelope: CommandEnvelope) -> Dict[str, Any]:
        append_log(self.log_path, "EXEC", f"Executando placa={envelope.plate} objetivo={envelope.objective}")
        complexity = float(envelope.metadata.get("complexity", 10.0))
        compressed = compress_complexity_logarithmically(complexity)

        if envelope.plate == "collect":
            result = self._collect(envelope, compressed)
        elif envelope.plate == "sanitize":
            result = self._sanitize(envelope, compressed)
        elif envelope.plate == "analyze":
            result = self._analyze(envelope, compressed)
        elif envelope.plate == "produce":
            result = self._produce(envelope, compressed)
        elif envelope.plate == "expose":
            result = self._expose(envelope, compressed)
        elif envelope.plate == "integrate":
            result = self._integrate(envelope, compressed)
        elif envelope.plate == "monitor":
            result = self._monitor(envelope, compressed)
        else:
            result = {
                "status": "ignored",
                "message": f"Placa desconhecida: {envelope.plate}",
                "compressed_complexity": compressed
            }

        return result

    def _collect(self, envelope: CommandEnvelope, compressed: float) -> Dict[str, Any]:
        payload = {
            "status": "ok",
            "objective": envelope.objective,
            "kind": "collection",
            "compressed_complexity": compressed,
            "items_found": envelope.metadata.get("expected_items", 0),
            "sources": envelope.metadata.get("sources", [])
        }
        save_json(self.results_dir / "collect_result.json", payload)
        return payload

    def _sanitize(self, envelope: CommandEnvelope, compressed: float) -> Dict[str, Any]:
        payload = {
            "status": "ok",
            "objective": envelope.objective,
            "kind": "sanitization",
            "compressed_complexity": compressed,
            "removed_duplicates": envelope.metadata.get("removed_duplicates", 0),
            "quarantined": envelope.metadata.get("quarantined", 0)
        }
        save_json(self.results_dir / "sanitize_result.json", payload)
        return payload

    def _analyze(self, envelope: CommandEnvelope, compressed: float) -> Dict[str, Any]:
        payload = {
            "status": "ok",
            "objective": envelope.objective,
            "kind": "analysis",
            "compressed_complexity": compressed,
            "insight": envelope.metadata.get("insight", "AnÃƒÆ'Ã‚Â¡lise concluÃƒÆ'Ã‚Â­da com critÃƒÆ'Ã‚Â©rio."),
            "commercial_value_score": envelope.metadata.get("commercial_value_score", 0.0)
        }
        save_json(self.results_dir / "analyze_result.json", payload)
        return payload

    def _produce(self, envelope: CommandEnvelope, compressed: float) -> Dict[str, Any]:
        payload = {
            "status": "ok",
            "objective": envelope.objective,
            "kind": "production",
            "compressed_complexity": compressed,
            "artifact_type": envelope.metadata.get("artifact_type", "unknown"),
            "artifact_name": envelope.metadata.get("artifact_name", "unnamed")
        }
        save_json(self.results_dir / "produce_result.json", payload)
        return payload

    def _expose(self, envelope: CommandEnvelope, compressed: float) -> Dict[str, Any]:
        payload = {
            "status": "ok",
            "objective": envelope.objective,
            "kind": "exposure",
            "compressed_complexity": compressed,
            "layer": envelope.metadata.get("layer", "enterprise_showcase"),
            "exposure_ready": envelope.metadata.get("exposure_ready", False)
        }
        save_json(self.commercial_dir / "expose_result.json", payload)
        return payload

    def _integrate(self, envelope: CommandEnvelope, compressed: float) -> Dict[str, Any]:
        payload = {
            "status": "ok",
            "objective": envelope.objective,
            "kind": "integration",
            "compressed_complexity": compressed,
            "client_system": envelope.metadata.get("client_system", "undefined"),
            "adapter": envelope.metadata.get("adapter_name", "undefined"),
            "contract": envelope.metadata.get("contract_name", "undefined"),
            "mapping": envelope.metadata.get("mapping_name", "undefined"),
            "auth_mode": envelope.metadata.get("auth_mode", "undefined"),
            "integration_strategy": envelope.metadata.get("integration_strategy", "contract-first")
        }
        save_json(self.integration_dir / "integrate_result.json", payload)
        return payload

    def _monitor(self, envelope: CommandEnvelope, compressed: float) -> Dict[str, Any]:
        payload = {
            "status": "ok",
            "objective": envelope.objective,
            "kind": "monitoring",
            "compressed_complexity": compressed,
            "health": "stable",
            "alerts": envelope.metadata.get("alerts", [])
        }
        save_json(self.results_dir / "monitor_result.json", payload)
        return payload


class Nucleus:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.config = load_json(CONFIG_PATH)
        self.logs_dir = ensure_dir(base_dir / self.config["paths"]["logs_dir"])
        self.snapshots_dir = ensure_dir(base_dir / self.config["paths"]["snapshots_dir"])
        self.log_path = self.logs_dir / "NUCLEUS_RUNTIME.log"
        self.atmosphere = AtmosphereFilter(self.config, self.log_path)
        self.gravity = GravityController(self.log_path)
        self.executor = PlateExecutor(base_dir, self.log_path)

    def describe(self) -> Dict[str, Any]:
        return {
            "ecosystem_name": self.config.get("ecosystem_name"),
            "version": self.config.get("version"),
            "base_dir": str(self.base_dir),
            "environment": env_info(),
            "plates": self.config.get("plates", [])
        }

    def decide(self, envelope: CommandEnvelope) -> Dict[str, Any]:
        append_log(self.log_path, "DECIDE", f"NÃƒÆ'Ã‚Âºcleo avaliando objetivo='{envelope.objective}' na placa='{envelope.plate}'")
        validation = self.atmosphere.validate(envelope)

        audit_payload = {
            "timestamp": now_iso(),
            "envelope": {
                "plate": envelope.plate,
                "objective": envelope.objective,
                "risk": envelope.risk,
                "confidence_inputs": envelope.confidence_inputs,
                "metadata": envelope.metadata
            },
            "validation": validation
        }
        write_snapshot(self.snapshots_dir, f"decision_{envelope.plate}", audit_payload)

        if validation["blocked"]:
            return {
                "status": "blocked",
                "plate": envelope.plate,
                "objective": envelope.objective,
                "validation": validation,
                "message": "ExecuÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o bloqueada pela atmosfera de proteÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o."
            }

        result = self.executor.execute(envelope)
        returned = self.gravity.pull_to_core(envelope.plate, result)

        final_payload = {
            "timestamp": now_iso(),
            "status": "completed",
            "plate": envelope.plate,
            "objective": envelope.objective,
            "validation": validation,
            "execution_result": result,
            "return_to_core": returned
        }
        write_snapshot(self.snapshots_dir, f"completed_{envelope.plate}", final_payload)
        return final_payload


def bootstrap_demo_cycles(nucleus: Nucleus, cycles: int = 1) -> List[Dict[str, Any]]:
    outputs: List[Dict[str, Any]] = []

    demo_envelopes: List[CommandEnvelope] = [
        CommandEnvelope(
            plate="collect",
            objective="Coletar sinais e ativos comerciais do reservatÃƒÆ'Ã‚Â³rio local",
            risk=0.20,
            confidence_inputs={
                "source_integrity": 0.90,
                "context_integrity": 0.88,
                "formula_support": 0.92
            },
            metadata={
                "expected_items": 12,
                "sources": ["Desktop", "Downloads", "ReservatÃƒÆ'Ã‚Â³rio IOTEC"],
                "complexity": 100
            }
        ),
        CommandEnvelope(
            plate="sanitize",
            objective="Sanear duplicados e isolar resÃƒÆ'Ã‚Â­duos sistÃƒÆ'Ã‚Âªmicos",
            risk=0.25,
            confidence_inputs={
                "source_integrity": 0.87,
                "context_integrity": 0.90,
                "formula_support": 0.91
            },
            metadata={
                "removed_duplicates": 5,
                "quarantined": 2,
                "complexity": 150
            }
        ),
        CommandEnvelope(
            plate="analyze",
            objective="Analisar valor comercial e aderÃƒÆ'Ã‚Âªncia do portfÃƒÆ'Ã‚Â³lio",
            risk=0.30,
            confidence_inputs={
                "source_integrity": 0.89,
                "context_integrity": 0.93,
                "formula_support": 0.95
            },
            metadata={
                "insight": "PortfÃƒÆ'Ã‚Â³lio apto para apresentaÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o seletiva e integraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o futura.",
                "commercial_value_score": 0.91,
                "complexity": 220
            }
        ),
        CommandEnvelope(
            plate="integrate",
            objective="Preparar integraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o com sistema do cliente",
            risk=0.35,
            confidence_inputs={
                "source_integrity": 0.95,
                "context_integrity": 0.94,
                "formula_support": 0.96
            },
            metadata={
                "client_system": "ERP_DO_CLIENTE",
                "adapter_name": "adapter_erp_cliente.py",
                "contract_name": "erp_cliente_contract.json",
                "mapping_name": "erp_cliente_mapping.json",
                "auth_mode": "api_key_or_oauth",
                "integration_strategy": "contract-first",
                "contract_defined": True,
                "mapping_defined": True,
                "formula_trusted": True,
                "complexity": 350
            }
        ),
        CommandEnvelope(
            plate="monitor",
            objective="Monitorar estabilidade do planeta sistÃƒÆ'Ã‚Âªmico",
            risk=0.10,
            confidence_inputs={
                "source_integrity": 0.90,
                "context_integrity": 0.91,
                "formula_support": 0.89
            },
            metadata={
                "alerts": [],
                "complexity": 50
            }
        )
    ]

    for _ in range(cycles):
        for envelope in demo_envelopes:
            outputs.append(nucleus.decide(envelope))

    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="NÃƒÆ'Ã‚Âºcleo Gravitacional IOTEC")
    parser.add_argument("--cycles", type=int, default=1, help="Quantidade de ciclos demonstrativos.")
    parser.add_argument("--describe", action="store_true", help="Exibe descriÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o do nÃƒÆ'Ã‚Âºcleo.")
    args = parser.parse_args()

    nucleus = Nucleus(BASE_DIR)

    if args.describe:
        print(json.dumps(nucleus.describe(), ensure_ascii=False, indent=2))
        return

    outputs = bootstrap_demo_cycles(nucleus, cycles=args.cycles)
    print(json.dumps(outputs, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()


