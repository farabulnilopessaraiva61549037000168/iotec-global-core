import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import plotly.graph_objects as go



def salvar_grafico(folha_atual, folha_nova, caminho):
    pass

    fig = go.Figure()

    fig.add_trace(go.Bar(

        x=["Atual", "Projetada"],

        y=[folha_atual, folha_nova],

        marker_color=["#1E6FFF", "#00C48C"]

    ))

    fig.update_layout(title="Folha: Atual vs Projetada")

    fig.write_image(caminho)  # requer kaleido: pip install kaleido







