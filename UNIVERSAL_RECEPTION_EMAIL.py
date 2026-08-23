import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
HTML = """

<!DOCTYPE html>
<html>

<head>

    <title>IBEX ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ IoTech</title>

    <meta charset="utf-8">

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{

            background:#050505;
            color:#f2f2f2;
            font-family:Arial;
            overflow-x:hidden;
        }

        .hero{

            height:100vh;

            background:
            linear-gradient(
                rgba(0,0,0,0.75),
                rgba(0,0,0,0.92)
            ),
            url('https://images.unsplash.com/photo-1500530855697-b586d89ba3ee');

            background-size:cover;
            background-position:center;

            display:flex;
            align-items:center;
            justify-content:center;

            text-align:center;

            padding:40px;
        }

        .hero-content{

            max-width:1000px;
        }

        .logo{

            font-size:90px;
            letter-spacing:14px;
            font-weight:bold;
        }

        .subtitle{

            margin-top:20px;
            font-size:22px;
            color:#bfbfbf;
            line-height:1.7;
        }

        .concept{

            margin-top:40px;
            font-size:18px;
            color:#888;
            line-height:1.9;
        }

        .reception-box{

            margin-top:40px;

            padding:18px 28px;

            border:1px solid #222;

            border-radius:18px;

            display:inline-block;

            background:rgba(255,255,255,0.03);

            backdrop-filter:blur(10px);
        }

        .reception-title{

            color:#888;

            font-size:13px;

            letter-spacing:3px;

            margin-bottom:10px;
        }

        .reception-email{

            font-size:18px;

            color:#f2f2f2;
        }

        .section{

            padding:90px 12%;
        }

        .title{

            font-size:42px;

            margin-bottom:20px;
        }

        .text{

            color:#aaaaaa;

            line-height:1.9;

            font-size:18px;
        }

        .grid{

            margin-top:60px;

            display:grid;

            grid-template-columns:
            repeat(auto-fit,minmax(250px,1fr));

            gap:30px;
        }

        .card{

            background:#0d0d0d;

            border:1px solid #1f1f1f;

            border-radius:24px;

            padding:35px;

            transition:0.3s;
        }

        .card:hover{

            transform:translateY(-6px);

            border-color:#666;
        }

        .card h3{

            margin-bottom:20px;

            font-size:24px;
        }

        .card p{

            color:#9f9f9f;

            line-height:1.7;
        }

        form{

            margin-top:50px;
        }

        input,
        textarea,
        select{

            width:100%;

            background:#0d0d0d;

            border:1px solid #222;

            border-radius:16px;

            padding:18px;

            color:#f2f2f2;

            margin-bottom:20px;

            font-size:16px;
        }

        textarea{

            min-height:180px;

            resize:vertical;
        }

        button{

            background:#f2f2f2;

            color:#000;

            border:none;

            padding:18px 40px;

            border-radius:14px;

            font-size:16px;

            cursor:pointer;

            transition:0.3s;
        }

        button:hover{

            transform:scale(1.03);
        }

        .footer{

            padding:50px;

            text-align:center;

            color:#666;

            border-top:1px solid #111;
        }

        .footer-logo{

            font-size:22px;

            letter-spacing:6px;

            margin-bottom:14px;
        }

        .footer-email{

            margin-top:12px;

            color:#999;
        }

    </style>

</head>

<body>

    <div class="hero">

        <div class="hero-content">

            <div class="logo">

                IBEX

            </div>

            <div class="subtitle">

                Precision ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ Intelligence ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ Altitude

            </div>

            <div class="concept">

                Estrutura analÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tica e tecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica
                voltada para modelagem,
                inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia operacional,
                visualizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gica
                e resoluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de gargalos tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnicos.

            </div>

            <div class="reception-box">

                <div class="reception-title">

                    UNIVERSAL RECEPTION

                </div>

                <div class="reception-email">

                    iotec.bl@proton.me

                </div>

            </div>

        </div>

    </div>

    <div class="section">

        <div class="title">

            Universal Reception ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ IoTech

        </div>

        <div class="text">

            Plataforma de recepÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o universal
            voltada para empresas,
            instituiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes,
            operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnicas
            e setores econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´micos.

            A estrutura IBEX recebe,
            organiza,
            analisa
            e direciona gargalos operacionais,
            tecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gicos
            e estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicos.

        </div>

        <div class="grid">

            <div class="card">

                <h3>Modelagem</h3>

                <p>

                    SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes,
                    cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios,
                    previsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes,
                    mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tricas
                    e anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise estrutural.

                </p>

            </div>

            <div class="card">

                <h3>GovernanÃƒÆ'Ã†â€™a</h3>

                <p>

                    OrganizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de fluxos,
                    auditoria,
                    rastreabilidade
                    e inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia operacional.

                </p>

            </div>

            <div class="card">

                <h3>VisualizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o</h3>

                <p>

                    Dashboards,
                    grÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ficos,
                    indicadores,
                    relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios
                    e painÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©is analÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos.

                </p>

            </div>

        </div>

        <form method="POST" action="/submit">

            <input
                type="text"
                name="empresa"
                placeholder="Empresa / InstituiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"
                required
            >

            <input
                type="email"
                name="email"
                placeholder="E-mail Corporativo"
                required
            >

            <input
                type="text"
                name="setor"
                placeholder="Setor EconÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mico"
                required
            >

            <input
                type="text"
                name="nome"
                placeholder="ResponsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel"
                required
            >

            <textarea
                name="gargalo"
                placeholder="Relate o gargalo tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico, operacional ou estrutural"
                required
            ></textarea>

            <button type="submit">

                ENVIAR PARA ANÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLISE

            </button>

        </form>

    </div>

    <div class="footer">

        <div class="footer-logo">

            IBEX

        </div>

        <div>

            Universal Reception ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ IoTech Platform

        </div>

        <div class="footer-email">

            iotec.bl@proton.me

        </div>

    </div>

</body>

</html>

"""




