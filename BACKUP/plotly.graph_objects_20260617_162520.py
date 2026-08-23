import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import plotly.graph_objects as go



def grafico_linha_premium(labels, y1, y2, titulo):
    pass

    fig = go.Figure()



    fig.add_trace(go.Scatter(

        x=labels, y=y1, name="Atual",

        mode="lines+markers",

        line=dict(color="#1E6FFF", width=3),

        marker=dict(size=6),

        fill="tozeroy",

        fillcolor="rgba(30,111,255,0.12)"

    ))



    fig.add_trace(go.Scatter(

        x=labels, y=y2, name="Projetado",

        mode="lines+markers",

        line=dict(color="#00C48C", width=3),

        marker=dict(size=6),

        fill="tozeroy",

        fillcolor="rgba(0,196,140,0.12)"

    ))



    fig.update_layout(title=titulo)

    return fig





