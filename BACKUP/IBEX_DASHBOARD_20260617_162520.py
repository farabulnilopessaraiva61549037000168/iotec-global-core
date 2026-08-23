import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IBEX DASHBOARD SYSTEM
# ============================================================
# OBJETIVO:
#
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â conectar nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo + interface
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â carregar JSON do stress test
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â gerar dashboard web
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â visual corporativo escuro
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â grÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ficos automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ticos
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â arquitetura modular
#
# REQUER:
#
# pip install flask plotly pandas
#
# EXECUTAR:
#
# python app.py
#
# ABRIR:
#
# http://127.0.0.1:5000
#
# ============================================================

from flask import Flask, render_template_string
import json
import pandas as pd
from pathlib import Path
import plotly.graph_objs as go
import plotly.offline as pyo

# ============================================================
# CONFIG
# ============================================================

DATA_FILE = Path("IBEX_OUTPUT/ibex_results.json")

app = Flask(__name__)

# ============================================================
# LOAD DATA
# ============================================================

def load_data():
    pass

    if not DATA_FILE.exists():
        pass

        return pd.DataFrame()

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        pass

        data = json.load(f)

    return pd.DataFrame(data)

# ============================================================
# BUILD CHART
# ============================================================

def build_chart(df):
    pass

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(
            y=df["robustness"],
            mode='lines',
            name='Robustness'
        )
    )

    fig.add_trace(

        go.Scatter(
            y=df["volatility"],
            mode='lines',
            name='Volatility'
        )
    )

    fig.update_layout(

        paper_bgcolor="#050505",
        plot_bgcolor="#050505",

        font=dict(
            color="#d9d9d9"
        ),

        title="IBEX CORE ANALYTICS",

        xaxis=dict(
            gridcolor="#222"
        ),

        yaxis=dict(
            gridcolor="#222"
        ),

        height=500
    )

    return pyo.plot(
        fig,
        output_type='div',
        include_plotlyjs='cdn'
    )

# ============================================================
# METRICS
# ============================================================

def metrics(df):
    pass

    return {

        "scenario_count":
            len(df),

        "avg_robustness":
            round(df["robustness"].mean(), 4),

        "avg_volatility":
            round(df["volatility"].mean(), 4),

        "max_robustness":
            round(df["robustness"].max(), 4),

        "min_robustness":
            round(df["robustness"].min(), 4),

        "avg_balance":
            round(df["market_balance"].mean(), 4)
    }

# ============================================================
# HTML TEMPLATE
# ============================================================

TEMPLATE = """

<!DOCTYPE html>
<html>

<head>

    <title>IBEX CORE</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{

            background:#050505;
            color:#d9d9d9;

            font-family:Arial;

            overflow-x:hidden;
        }

        .hero{

            height:100vh;

            background:
            linear-gradient(
                rgba(0,0,0,0.7),
                rgba(0,0,0,0.9)
            ),
            url('https://images.unsplash.com/photo-1506744038136-46273834b3fb');

            background-size:cover;
            background-position:center;

            display:flex;
            align-items:center;
            justify-content:center;

            text-align:center;
        }

        .hero h1{

            font-size:90px;

            letter-spacing:12px;

            color:#ffffff;
        }

        .hero p{

            margin-top:20px;

            font-size:20px;

            color:#aaaaaa;
        }

        .section{

            padding:80px;
        }

        .cards{

            display:grid;

            grid-template-columns:
            repeat(auto-fit,minmax(250px,1fr));

            gap:25px;

            margin-top:40px;
        }

        .card{

            background:#111;

            border:1px solid #222;

            border-radius:20px;

            padding:30px;

            transition:0.3s;
        }

        .card:hover{

            transform:translateY(-5px);

            border-color:#888;
        }

        .metric{

            font-size:40px;

            margin-top:15px;

            color:#ffffff;
        }

        .chart{

            margin-top:50px;
        }

        .footer{

            padding:40px;

            text-align:center;

            color:#666;
        }

    </style>

</head>

<body>

    <div class="hero">

        <div>

            <h1>IBEX</h1>

            <p>
            Precision ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Altitude ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Intelligence
            </p>

        </div>

    </div>

    <div class="section">

        <h2>CORE METRICS</h2>

        <div class="cards">

            {% for key,value in metrics.items() %}

            <div class="card">

                <h3>{{ key }}</h3>

                <div class="metric">

                    {{ value }}

                </div>

            </div>

            {% endfor %}

        </div>

        <div class="chart">

            {{ chart|safe }}

        </div>

    </div>

    <div class="footer">

        IBEX CORE ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ IoTech Platform

    </div>

</body>

</html>

"""

# ============================================================
# ROUTE
# ============================================================

@app.route("/")

def index():
    pass

    df = load_data()

    if df.empty:
        pass

        return "NO DATA"

    chart = build_chart(df)

    data_metrics = metrics(df)

    return render_template_string(

        TEMPLATE,

        chart=chart,

        metrics=data_metrics
    )

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    print("\n===================================")
    print(" IBEX DASHBOARD ONLINE")
    print("===================================\n")

    app.run(
        debug=False, use_reloader=False
    )


