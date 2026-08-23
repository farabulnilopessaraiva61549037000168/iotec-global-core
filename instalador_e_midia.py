import sys
import subprocess
import os

# ------------------------------------------------------------------------------
# 1. INSTALADOR AUTOMÁTICO DE PACOTES (PIP INSTALLER)
# ------------------------------------------------------------------------------
pacotes_necessarios = [
    "requests",       # Para requisições HTTP e consumo de APIs
    "beautifulsoup4", # Para raspagem/extração de dados de portais institucionais
    "urllib3"         # Auxiliar para downloads e conexões puras
]

def instalar_pacotes():
    print("[*] Verificando e instalando dependências PIP automaticamente...")
    for pacote in pacotes_necessarios:
        try:
            __import__(pacote)
            print(f" -> Pacote '{pacote}' já está instalado.")
        except ImportError:
            print(f" -> Instalando '{pacote}'...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

instalar_pacotes()

import requests

# ------------------------------------------------------------------------------
# 2. MAPEAMENTO DE INSTITUIÇÕES CORPORATIVAS E CERTIDÕES (APIs / URLS)
# ------------------------------------------------------------------------------
INSTITUICOES_E_CERTIDOES = {
    "Receita Federal (CNPJ / CND)": "https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/Emitir",
    "JUCESP (Junta Comercial SP)": "https://www.jucesp.sp.gov.br/",
    "Caixa Econômica (CRF FGTS)": "https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf",
    "Simples Nacional": "https://www8.receita.fazenda.gov.br/SimplesNacional/aplicacoes/atbpo/dte.app/",
    "Portal de Certidões Digitais": "https://www.registrodeimoveis.org.br/"
}

def exibir_links_institucionais():
    print("\n" + "="*70)
    print("MAPEAMENTO DE INSTITUIÇÕES CORPORATIVAS E EMISSÃO DE CERTIDÕES")
    print("="*70)
    for nome, url in INSTITUICOES_E_CERTIDOES.items():
        print(f"• {nome.ljust(30)} : {url}")

# ------------------------------------------------------------------------------
# 3. DOWNLOAD AUTOMÁTICO DE VÍDEOS DE PLANO DE FUNDO (TI, IA, CORPORATIVO)
# ------------------------------------------------------------------------------
def baixar_videos_plano_de_fundo():
    print("\n" + "="*70)
    print("DOWNLOAD DE VÍDEOS GRATUITOS (PANO DE FUNDO: TI / IA / CORPORATIVO)")
    print("="*70)
    
    pasta_destino = "./midias_fundo"
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Exemplo de vídeos de alta qualidade de uso livre (Stock / Royalty Free)
    videos_gratuitos = [
        {
            "nome": "fundo_tecnologia_servidores.mp4",
            "url": "https://assets.mixkit.co/videos/preview/mixkit-data-center-room-with-server-racks-42848-large.mp4",
            "categoria": "TI / Servidores"
        },
        {
            "nome": "fundo_inteligencia_artificial.mp4",
            "url": "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-data-41539-large.mp4",
            "categoria": "Inteligência Artificial"
        },
        {
            "nome": "fundo_corporativo_escritorio.mp4",
            "url": "https://assets.mixkit.co/videos/preview/mixkit-people-working-in-a-modern-office-4330-large.mp4",
            "categoria": "Corporativo"
        }
    ]

    for item in videos_gratuitos:
        caminho_arquivo = os.path.join(pasta_destino, item["nome"])
        print(f"[*] Baixando vídeo [{item['categoria']}]: {item['nome']}...")
        
        try:
            resposta = requests.get(item["url"], stream=True, timeout=30)
            if resposta.status_code == 200:
                with open(caminho_arquivo, "wb") as f:
                    for chunk in resposta.iter_content(chunk_size=1024*1024):
                        if chunk:
                            f.write(chunk)
                print(f"    [OK] Salvo em: {caminho_arquivo}")
            else:
                print(f"    [ERRO] Falha ao baixar (Código HTTP: {resposta.status_code})")
        except Exception as e:
            print(f"    [ERRO] Ocorreu uma exceção durante o download: {e}")

# ------------------------------------------------------------------------------
# EXECUÇÃO DO SCRIPT
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    exibir_links_institucionais()
    baixar_videos_plano_de_fundo()
    print("\nProcesso concluído com sucesso!")