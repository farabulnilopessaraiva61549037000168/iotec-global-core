"""
===================================================================================
             IOTEC NUCLEUS - MALHA CELESTE & GEOINTELIGÊNCIA B2B
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 CNPJ: 61.549.037/0001-68 | WhatsApp Corporativo: (88) 99930-6416
===================================================================================
"""

import urllib.request
import json
import manifest

class MalhaCeleste:
    def __init__(self):
        self.provedor = "OpenStreetMap / Overpass Geoint Engine"

    def mapear_coordenadas_alvo(self, razao_social: str, cidade: str, uf: str = "CE"):
        query_str = f"{razao_social}, {cidade}, {uf}, Brasil"
        url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query_str)}&format=json&limit=1"
        
        headers = {'User-Agent': 'IOTEC_Nucleus_Geoint/1.0 (farabulini@iotec.com)'}
        req = urllib.request.Request(url, headers=headers)
        
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                if data:
                    lat = data[0]['lat']
                    lon = data[0]['lon']
                    print(f"[📡 SATÉLITE CONECTADO] {razao_social} em {cidade}/{uf}")
                    print(f"    └── Coordenadas Fixadas: Lat {lat} | Lon {lon}")
                    print(f"    └── Link Radar Celeste: https://www.google.com/maps/@{lat},{lon},18z/data=!3m1!1e3\n")
                    return {"lat": lat, "lon": lon}
                else:
                    print(f"[⚠️ SATÉLITE] Busca genérica para município: {cidade}/{uf}...")
                    return None
        except Exception as e:
            print(f"[❌ ERRO MALHA CELESTE]: {e}")
            return None

if __name__ == "__main__":
    manifest.exibir_banner_identidade()
    print("[🛰️] ATIVANDO VARREDURA DA MALHA CELESTE - SENSORIAMENTO REMOTO\n")
    radar = MalhaCeleste()
    
    # Teste de travamento de satélite nos alvos
    alvos = [
        ("Pinheiro Supermercados", "Quixadá"),
        ("Avine Alimentos", "Quixeramobim"),
        ("Distribuidora Jaguaribe", "Russas")
    ]
    
    for empresa, cidade in alvos:
        radar.mapear_coordenadas_alvo(empresa, cidade)