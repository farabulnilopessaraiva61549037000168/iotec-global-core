import json
import os
from datetime import datetime

# ==========================================================
# IOTEC CONNECTOR ORCHESTRATOR
# ==========================================================

CONNECTORS = [
    {
        "name": "Google Maps",
        "priority": 1,
        "enabled": False,
        "capability": "company_discovery"
    },
    {
        "name": "OpenStreetMap",
        "priority": 2,
        "enabled": True,
        "capability": "company_discovery"
    },
    {
        "name": "Corporate CSV",
        "priority": 3,
        "enabled": True,
        "capability": "company_discovery"
    },
    {
        "name": "Corporate Excel",
        "priority": 4,
        "enabled": True,
        "capability": "company_discovery"
    }
]


def choose_connector(capability):
    available = [
        c for c in CONNECTORS
        if c["enabled"] and c["capability"] == capability
    ]

    if not available:
        return None

    available.sort(key=lambda x: x["priority"])
    return available[0]


def build_report(selected):

    report = {
        "generated_at": datetime.now().isoformat(),
        "selected_connector": None,
        "connectors": CONNECTORS
    }

    if selected:
        report["selected_connector"] = selected["name"]

    with open(
        "IOTEC_CONNECTOR_STATUS.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


def print_console(selected):

    print("=" * 80)
    print("IOTEC CONNECTOR ORCHESTRATOR")
    print("=" * 80)
    print()

    print("MISSION")
    print("-" * 80)
    print("Company Discovery")
    print()

    print("CONNECTORS")
    print("-" * 80)

    for c in sorted(CONNECTORS, key=lambda x: x["priority"]):

        status = "ONLINE" if c["enabled"] else "OFFLINE"

        print(
            f"{c['priority']:02d} | "
            f"{c['name']:<20} | "
            f"{status}"
        )

    print()

    print("-" * 80)

    if selected:

        print("SELECTED CONNECTOR")
        print(selected["name"])

    else:

        print("NO CONNECTOR AVAILABLE")

    print()

    print("OUTPUT FILE")
    print("IOTEC_CONNECTOR_STATUS.json")

    print()

    print("STATUS")
    print("CONNECTOR ORCHESTRATION READY")


def main():

    selected = choose_connector("company_discovery")

    build_report(selected)

    print_console(selected)


if __name__ == "__main__":
    main()

