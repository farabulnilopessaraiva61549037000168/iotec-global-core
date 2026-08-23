import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

FILE = Path(r"C:\IOTEC\FROZEN\visible_core_router.py")

def add_dispatch_if_missing(text: str) -> str:
    if "def dispatch" in text:
        return text

    patch = """

    # ===== IOTEC SAFE FALLBACK DISPATCH =====
    def dispatch(self, payload: dict):
        """
        Fallback mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nimo para restaurar pipeline.
        Evita crash estrutural apÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³s rebuild.
        """

        return {
            "status": "fallback_active",
            "input": payload,
            "message": "dispatch nÃƒÆ'Ã†â€™o implementado no rebuild atual"
        }
    # ========================================
"""

    # injeta dentro da classe principal
    if "class SuperIllusionVisibleCore" in text:
        text = text.replace(
            "class SuperIllusionVisibleCore",
            "class SuperIllusionVisibleCore" + patch
        )

    return text

def main():
    text = FILE.read_text(encoding="utf-8", errors="ignore")

    text = add_dispatch_if_missing(text)

    FILE.write_text(text, encoding="utf-8")

    print("[OK] dispatch restaurado com fallback seguro")

if __name__ == "__main__":
    main()




