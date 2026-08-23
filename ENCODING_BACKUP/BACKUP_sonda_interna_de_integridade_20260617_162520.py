import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import socket
import hashlib
import platform
import urllib.request
import urllib.error
import shutil
from pathlib import Path
from datetime import datetime

APP_NAME = "Sonda de Integridade Interna"
APP_VERSION = "1.0.0"

# =========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DA SONDAGEM
# =========================
CONFIG = {
    "required_files": [
        "app.py",
        ".env",
        "requirements.txt",
    ],
    "required_directories": [
        "logs",
        "data",
    ],
    "required_env_vars": [
        "APP_ENV",
        "APP_PORT",
    ],
    "tcp_services": [
        {"name": "Banco PostgreSQL", "host": "127.0.0.1", "port": 5432, "timeout": 3},
        {"name": "Redis", "host": "127.0.0.1", "port": 6379, "timeout": 3},
    ],
    "http_endpoints": [
        {"name": "API Health", "url": "http://127.0.0.1:8000/health", "timeout": 5, "expected_status": 200},
    ],
    "disk_threshold_percent": 90,
    "memory_threshold_percent": 90,
    "critical_hash_files": [
        # Exemplo:
        # {"path": "config/settings.yml", "sha256": "COLE_O_HASH_AQUI"}
    ]
}


# =========================
# ESTRUTURA DE RESULTADOS
# =========================
def result_item(name, status, details, category="general"):
    return {
        "name": name,
        "status": status,   # PASS | WARN | FAIL
        "details": details,
        "category": category,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


# =========================
# CHECKS
# =========================
def check_required_files():
    results = []
    for file_path in CONFIG["required_files"]:
        p = Path(file_path)
        if p.is_file():
            results.append(result_item(
                f"Arquivo obrigatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio: {file_path}",
                "PASS",
                f"Arquivo encontrado em {p.resolve()}",
                "files"
            ))
        else:
            results.append(result_item(
                f"Arquivo obrigatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio: {file_path}",
                "FAIL",
                "Arquivo nÃƒÆ'Ã†â€™o encontrado",
                "files"
            ))
    return results


def check_required_directories():
    results = []
    for dir_path in CONFIG["required_directories"]:
        p = Path(dir_path)
        if p.is_dir():
            results.append(result_item(
                f"DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio obrigatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio: {dir_path}",
                "PASS",
                f"DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio encontrado em {p.resolve()}",
                "directories"
            ))
        else:
            results.append(result_item(
                f"DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio obrigatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio: {dir_path}",
                "FAIL",
                "DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio nÃƒÆ'Ã†â€™o encontrado",
                "directories"
            ))
    return results


def check_env_vars():
    results = []
    for var in CONFIG["required_env_vars"]:
        value = os.getenv(var)
        if value is None or str(value).strip() == "":
            results.append(result_item(
                f"VariÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel de ambiente: {var}",
                "FAIL",
                "VariÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel ausente ou vazia",
                "environment"
            ))
        else:
            results.append(result_item(
                f"VariÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel de ambiente: {var}",
                "PASS",
                "VariÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel presente",
                "environment"
            ))
    return results


def check_tcp_services():
    results = []
    for svc in CONFIG["tcp_services"]:
        name = svc["name"]
        host = svc["host"]
        port = svc["port"]
        timeout = svc.get("timeout", 3)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        start = time.time()

        try:
            sock.connect((host, port))
            elapsed = round((time.time() - start) * 1000, 2)
            results.append(result_item(
                f"TCP: {name}",
                "PASS",
                f"ConexÃƒÆ'Ã†â€™o OK em {elapsed} ms ({host}:{port})",
                "network"
            ))
        except Exception as e:
            results.append(result_item(
                f"TCP: {name}",
                "FAIL",
                f"Falha ao conectar em {host}:{port} -> {str(e)}",
                "network"
            ))
        finally:
            sock.close()

    return results


def check_http_endpoints():
    results = []
    for ep in CONFIG["http_endpoints"]:
        name = ep["name"]
        url = ep["url"]
        timeout = ep.get("timeout", 5)
        expected_status = ep.get("expected_status", 200)

        req = urllib.request.Request(url, headers={"User-Agent": "IntegrityProbe/1.0"})
        start = time.time()

        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                status_code = response.getcode()
                elapsed = round((time.time() - start) * 1000, 2)

                if status_code == expected_status:
                    results.append(result_item(
                        f"HTTP: {name}",
                        "PASS",
                        f"Status {status_code} em {elapsed} ms -> {url}",
                        "http"
                    ))
                else:
                    results.append(result_item(
                        f"HTTP: {name}",
                        "WARN",
                        f"Status inesperado: {status_code}, esperado: {expected_status}",
                        "http"
                    ))
        except urllib.error.HTTPError as e:
            results.append(result_item(
                f"HTTP: {name}",
                "FAIL",
                f"HTTPError {e.code} -> {url}",
                "http"
            ))
        except Exception as e:
            results.append(result_item(
                f"HTTP: {name}",
                "FAIL",
                f"Falha na requisiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o -> {str(e)}",
                "http"
            ))

    return results


def check_disk_usage():
    results = []
    total, used, free = shutil.disk_usage("/")
    used_percent = round((used / total) * 100, 2)

    threshold = CONFIG["disk_threshold_percent"]
    if used_percent >= threshold:
        status = "WARN"
        details = f"Uso de disco alto: {used_percent}% (limite configurado: {threshold}%)"
    else:
        status = "PASS"
        details = f"Uso de disco saudÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel: {used_percent}%"

    results.append(result_item("Uso de disco", status, details, "system"))
    return results


def check_memory_usage():
    results = []
    try:
        import psutil  # opcional
        mem = psutil.virtual_memory()
        used_percent = round(mem.percent, 2)
        threshold = CONFIG["memory_threshold_percent"]

        if used_percent >= threshold:
            status = "WARN"
            details = f"Uso de memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria alto: {used_percent}% (limite configurado: {threshold}%)"
        else:
            status = "PASS"
            details = f"Uso de memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria saudÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel: {used_percent}%"

        results.append(result_item("Uso de memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria", status, details, "system"))

    except ImportError:
        results.append(result_item(
            "Uso de memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria",
            "WARN",
            "psutil nÃƒÆ'Ã†â€™o instalado; verificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o detalhada de memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria ignorada",
            "system"
        ))
    return results


def check_file_hashes():
    results = []
    for item in CONFIG["critical_hash_files"]:
        path = item["path"]
        expected = item["sha256"]

        if not Path(path).is_file():
            results.append(result_item(
                f"Hash arquivo crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico: {path}",
                "FAIL",
                "Arquivo crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico nÃƒÆ'Ã†â€™o encontrado",
                "integrity"
            ))
            continue

        try:
            current = sha256_file(path)
            if current.lower() == expected.lower():
                results.append(result_item(
                    f"Hash arquivo crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico: {path}",
                    "PASS",
                    "Integridade confirmada por SHA256",
                    "integrity"
                ))
            else:
                results.append(result_item(
                    f"Hash arquivo crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico: {path}",
                    "FAIL",
                    f"Hash divergente. Atual: {current}",
                    "integrity"
                ))
        except Exception as e:
            results.append(result_item(
                f"Hash arquivo crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico: {path}",
                "FAIL",
                f"Erro ao calcular hash: {str(e)}",
                "integrity"
            ))

    if not CONFIG["critical_hash_files"]:
        results.append(result_item(
            "Hash de arquivos crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos",
            "WARN",
            "Nenhum arquivo crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico configurado para validaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de hash",
            "integrity"
        ))
    return results


def system_metadata():
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "hostname": platform.node(),
        "platform": platform.platform(),
        "python_version": sys.version,
        "utc_time": datetime.utcnow().isoformat() + "Z",
        "cwd": str(Path.cwd())
    }


def summarize(results):
    summary = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for item in results:
        summary[item["status"]] += 1

    if summary["FAIL"] > 0:
        overall = "NOT_READY"
    elif summary["WARN"] > 0:
        overall = "READY_WITH_WARNINGS"
    else:
        overall = "READY"

    return overall, summary


def main():
    all_results = []

    all_results.extend(check_required_files())
    all_results.extend(check_required_directories())
    all_results.extend(check_env_vars())
    all_results.extend(check_tcp_services())
    all_results.extend(check_http_endpoints())
    all_results.extend(check_disk_usage())
    all_results.extend(check_memory_usage())
    all_results.extend(check_file_hashes())

    overall, summary = summarize(all_results)

    report = {
        "metadata": system_metadata(),
        "overall_status": overall,
        "summary": summary,
        "results": all_results
    }

    report_name = f"integrity_report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_name, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"\nRelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo em: {report_name}")

    if overall == "NOT_READY":
        sys.exit(2)
    elif overall == "READY_WITH_WARNINGS":
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()


