import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from core_ai.chat_interface import start_chat
from seo_manager.wix_api_integration import WixSEOManager
from domain_manager.domain_api import DomainManager
from forensic_module.log_analyzer import LogAnalyzer
from consultancy_engine.project_generator import ProjectGenerator

def main():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ NeoComplex Nova IA iniciado...")

    # Iniciar mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo de chat IA
    start_chat()

    # SEO automation example
    wix = WixSEOManager(api_key="YOUR_WIX_API_KEY")
    response = wix.update_meta_description(site_id="123456", description="SoluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes em dados e IA aplicada")
    print("SEO atualizado:", response)

    # Iniciar mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo de projetos
    generator = ProjectGenerator()
    project = generator.generate("AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de trÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡fego urbano com IA")
    print("Projeto gerado:", project)

    # Forense digital exemplo
    analyzer = LogAnalyzer()
    report = analyzer.analyze("server_logs.log")
    print("RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio Forense:", report)

if __name__ == "__main__":
    main()


