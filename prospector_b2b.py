"""
===================================================================================
                       IOTEC NUCLEUS - PROSPECTOR B2B LOCALHOST
               MÓDULO DE INTELIGÊNCIA COMERCIAL E CAPTURA DE SOCIOS
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 Entidade Proprietária: CNPJ 61.549.037/0001-68
===================================================================================
"""

import urllib.request
import json
import time
from typing import Dict, Any, List

class ProspectorB2B:
    def __init__(self):
        self.api_base = "https://publica.cnpj.ws/cnpj/"

    def consultar_cnpj_real(self, cnpj: str) -> Dict[str, Any]:
        """
        Consulta dados públicos de qualquer CNPJ no Brasil (Sem custos de API).
        """
        cnpj_limpo = str(cnpj).replace(".", "").replace("/", "").replace("-", "").strip()
        url = f"{self.api_base}{cnpj_limpo}"

        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )

        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    return self._processar_dados_empresa(data)
        except Exception as e:
            print(f"[!] Erro ao consultar CNPJ {cnpj_limpo}: {e}")
            return {}

    def _processar_dados_empresa(self, data: Dict[str, Any]) -> Dict[str, Any]:
        razao_social = data.get("razao_social", "N/A")
        estabelecimento = data.get("estabelecimento", {})
        
        # Sócios / Empresários
        socios = []
        for s in data.get("socios", []):
            socios.append({
                "nome": s.get("nome"),
                "qualificacao": s.get("qualificacao", {}).get("descricao")
            })

        # Contatos Comerciais
        email = estabelecimento.get("email")
        ddd = estabelecimento.get("ddd1")
        telefone = estabelecimento.get("telefone1")
        telefone_completo = f"({ddd}) {telefone}" if ddd and telefone else "N/A"

        # Atividade Principal
        atividade = estabelecimento.get("atividade_principal", {}).get("descricao", "N/A")

        return {
            "cnpj": data.get("cnpj_raiz"),
            "razao_social": razao_social,
            "nome_fantasia": estabelecimento.get("nome_fantasia", razao_social),
            "atividade": atividade,
            "telefone": telefone_completo,
            "email": email,
            "socios_decisores": socios,
            "cidade": estabelecimento.get("cidade", {}).get("nome"),
            "uf": estabelecimento.get("estado", {}).get("sigla")
        }

if __name__ == "__main__":
    prospector = ProspectorB2B()
    print("\n[+] INICIANDO CAPTURA DE EMPRESAS E DECISORES EM LOCALHOST...\n")
    
    # Exemplo de consulta com CNPJ real (Alvo de exemplo ou seu próprio CNPJ/Parceiros)
    cnpj_alvo = "61549037000168"  # IOTEC
    resultado = prospector.consultar_cnpj_real(cnpj_alvo)

    print("┌" + "─" * 73 + "┐")
    print(f"│ EMPRESA     : {resultado.get('razao_social', 'N/A'):<55} │")
    print(f"│ CIDADE/UF   : {resultado.get('cidade', 'N/A')}/{resultado.get('uf', 'N/A'):<53} │")
    print(f"│ CONTATO     : {resultado.get('telefone', 'N/A'):<55} │")
    print(f"│ E-MAIL      : {resultado.get('email', 'N/A'):<55} │")
    print("├" + "─" * 73 + "┤")
    print("│ SOCIOS E DECISORES IDENTIFICADOS:                                      │")
    for socio in resultado.get("socios_decisores", []):
        print(f"│   - {socio['nome']} ({socio['qualificacao']})")
    print("└" + "─" * 73 + "┘\n")