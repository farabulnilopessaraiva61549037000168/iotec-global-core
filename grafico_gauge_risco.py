import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def grafico_gauge_risco(valor, titulo="NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­vel de Risco"):
    pass

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=valor,

        title={'text': titulo},

        gauge={

            'axis': {'range': [0, 100]},

            'bar': {'color': "#1E6FFF"},

            'steps': [

                {'range': [0, 33], 'color': "rgba(0,196,140,0.3)"},

                {'range': [33, 66], 'color': "rgba(255,176,32,0.3)"},

                {'range': [66, 100], 'color': "rgba(255,77,79,0.3)"}

            ],

        }

    ))

    return fig







