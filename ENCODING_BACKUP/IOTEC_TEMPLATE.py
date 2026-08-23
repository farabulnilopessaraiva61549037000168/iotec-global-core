import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import plotly.io as pio

IOTEC_TEMPLATE = dict(
    layout=dict(
        paper_bgcolor="#0B0F14",
        plot_bgcolor="#0B0F14",
        font=dict(color="#E6EDF3", family="Inter"),
        title=dict(x=0.02, xanchor="left", font=dict(size=20)),
        margin=dict(l=40, r=20, t=60, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)", zeroline=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)", zeroline=False),
    )
)

pio.templates["iotec"] = IOTEC_TEMPLATE
pio.templates.default = "iotec"



