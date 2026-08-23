import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==============================
# IOTEC UPGRADE MODULE (NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ALTERA BASE)
# ==============================

def adicionar_camadas_mapa(self, mapa):
    """
    Adiciona camadas extras sem alterar o mapa original
    """

    # Camada escura (modo tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico)
    folium.TileLayer('CartoDB dark_matter').add_to(mapa)

    # Camada padrÃƒÆ'Ã†â€™o (ruas)
    folium.TileLayer('OpenStreetMap').add_to(mapa)

    # Controle de camadas
    folium.LayerControl().add_to(mapa)


def adicionar_marcadores_taticos(self, mapa, dados):
    """
    Adiciona indicadores mais visuais sem remover os existentes
    """

    for d in dados[-15:]:
        folium.CircleMarker(
            location=d["coords"],
            radius=8,
            color="#00e5ff",
            fill=True,
            fill_opacity=0.25,
            popup=(
                f"<b>Tipo:</b> {d['tipo']}<br>"
                f"<b>Cidade:</b> {d['cidade']}<br>"
                f"<b>Hora:</b> {d['hora']}"
            )
        ).add_to(mapa)


def enriquecer_alertas(self, ocorrencia):
    """
    Adiciona contexto sem alterar o alerta original
    """

    self.alertas.append(
        f"RegiÃƒÆ'Ã†â€™o monitorada: {ocorrencia['regiao']} | {ocorrencia['cidade']}"
    )


def enriquecer_analise(self):
    """
    Complementa a IA existente
    """

    self.ia.append(
        f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Ârea ativa: {self.regiao_atual}"
    )


def ajustar_zoom_inteligente(self, mapa, dados):
    """
    Centraliza automaticamente na ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rea com mais ocorrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias
    """

    if not dados:
        return mapa

    contagem = {}
    for d in dados:
        cidade = d["cidade"]
        contagem[cidade] = contagem.get(cidade, 0) + 1

    cidade_top = max(contagem, key=contagem.get)

    for d in dados:
        if d["cidade"] == cidade_top:
            mapa.location = d["coords"]
            break

    return mapa


