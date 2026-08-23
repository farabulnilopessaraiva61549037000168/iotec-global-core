import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def grafico_barras_premium(labels, valores, titulo):
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=labels,
        y=valores,
        marker=dict(
            color=valores,
            colorscale=[[0, "#1E6FFF"], [1, "#00C48C"]],
            line=dict(color="rgba(255,255,255,0.08)", width=1)
        ),
        text=[f"R$ {v:,.0f}" for v in valores],
        textposition="outside"
    ))

    fig.update_layout(title=titulo, yaxis=dict(tickprefix="R$ "))
    return fig



