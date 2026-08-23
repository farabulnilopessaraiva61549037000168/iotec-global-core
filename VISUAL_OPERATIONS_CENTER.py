import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC EXECUTIVE VISUAL OPERATIONS CENTER

# CENTRAL VISUAL CINEMATOGRAFICA

# =========================================================



from flask import Flask



from flask_cors import CORS



app = Flask(__name__)



CORS(app)



# =========================================================

# HTML

# =========================================================



HTML = """



<!DOCTYPE html>



<html lang="pt-br">



<head>



<meta charset="UTF-8">



<meta name="viewport" content="width=device-width, initial-scale=1.0">



<title>IOTEC EXECUTIVE VISUAL CENTER</title>



<style>



*{

    margin:0;

    padding:0;

    box-sizing:border-box;

    font-family:Arial;

}



body{



    background:#05070d;



    color:white;



    overflow:hidden;

}



.header{



    width:100%;



    height:90px;



    background:linear-gradient(

        90deg,

        #07111f,

        #0b1d33,

        #07111f

    );



    display:flex;



    align-items:center;



    justify-content:space-between;



    padding:0 40px;



    border-bottom:1px solid #1d4f91;

}



.logo{



    font-size:34px;



    font-weight:bold;



    letter-spacing:2px;



    color:#5bc0ff;

}



.subtitle{



    color:#6f9dc9;



    font-size:14px;

}



.status{



    display:flex;



    gap:15px;

}



.status-box{



    background:#08131f;



    padding:12px 18px;



    border-radius:10px;



    border:1px solid #173657;



    min-width:130px;



    text-align:center;

}



.status-title{



    font-size:12px;



    color:#7aa6d1;

}



.status-value{



    margin-top:5px;



    font-size:20px;



    color:#63ffae;

}



.main{



    display:grid;



    grid-template-columns:25% 50% 25%;



    height:calc(100vh - 90px);

}



.left-panel,

.right-panel{



    padding:20px;



    background:#07111c;



    overflow:auto;

}



.center-panel{



    padding:20px;



    background:#03060c;



    display:flex;



    flex-direction:column;



    gap:20px;

}



.card{



    background:#08131f;



    border:1px solid #173657;



    border-radius:16px;



    padding:20px;



    margin-bottom:20px;



    box-shadow:0 0 25px rgba(0,0,0,0.4);

}



.card-title{



    font-size:18px;



    margin-bottom:15px;



    color:#58b8ff;

}



.service{



    display:flex;



    justify-content:space-between;



    margin-bottom:10px;



    padding:12px;



    background:#0d1a2b;



    border-radius:10px;

}



.online{



    color:#63ffae;

}



.offline{



    color:#ff5f5f;

}



.tower{



    flex:1;



    background:linear-gradient(

        180deg,

        #091321,

        #03060c

    );



    border-radius:20px;



    border:1px solid #1c4777;



    position:relative;



    overflow:hidden;

}



.tower::before{



    content:"";



    position:absolute;



    width:600px;



    height:600px;



    background:radial-gradient(

        circle,

        rgba(0,153,255,0.25),

        transparent

    );



    top:-150px;



    left:50%;



    transform:translateX(-50%);

}



.center-title{



    position:absolute;



    top:40px;



    left:50%;



    transform:translateX(-50%);



    font-size:42px;



    color:#63c7ff;



    font-weight:bold;



    letter-spacing:3px;

}



.layers{



    position:absolute;



    top:140px;



    left:50%;



    transform:translateX(-50%);



    width:80%;

}



.layer{



    height:80px;



    background:#08131f;



    border:1px solid #1d4f91;



    margin-bottom:20px;



    border-radius:14px;



    display:flex;



    align-items:center;



    justify-content:space-between;



    padding:0 30px;



    box-shadow:0 0 20px rgba(0,0,0,0.4);

}



.layer-name{



    font-size:22px;



    color:#72c4ff;

}



.layer-status{



    color:#63ffae;



    font-size:18px;

}



.footer{



    position:absolute;



    bottom:15px;



    width:100%;



    text-align:center;



    color:#4c6b8c;



    font-size:13px;

}



.alert{



    background:#1a1111;



    border:1px solid #7a2d2d;



    color:#ff8b8b;



    padding:12px;



    border-radius:10px;



    margin-bottom:10px;

}



.executive{



    background:#0d1a2b;



    border-radius:10px;



    padding:12px;



    margin-bottom:10px;

}



</style>



</head>



<body>



<div class="header">



    <div>



        <div class="logo">

            IOTEC CENTRAL OPERACIONAL

        </div>



        <div class="subtitle">

            PresidÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ GovernanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ ProduÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Observabilidade

        </div>



    </div>



    <div class="status">



        <div class="status-box">



            <div class="status-title">

                ECOSSISTEMA

            </div>



            <div class="status-value">

                ONLINE

            </div>



        </div>



        <div class="status-box">



            <div class="status-title">

                SERVIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡OS

            </div>



            <div class="status-value">

                6

            </div>



        </div>



        <div class="status-box">



            <div class="status-title">

                TORRE

            </div>



            <div class="status-value">

                ATIVA

            </div>



        </div>



    </div>



</div>



<div class="main">



    <div class="left-panel">



        <div class="card">



            <div class="card-title">

                SERVIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡OS OPERACIONAIS

            </div>



            <div class="service">

                <span>GovernanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a</span>

                <span class="online">ONLINE</span>

            </div>



            <div class="service">

                <span>PresidÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia</span>

                <span class="online">ONLINE</span>

            </div>



            <div class="service">

                <span>Curadoria</span>

                <span class="online">ONLINE</span>

            </div>



            <div class="service">

                <span>ConsolidaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o</span>

                <span class="online">ONLINE</span>

            </div>



            <div class="service">

                <span>Criatividade</span>

                <span class="online">ONLINE</span>

            </div>



            <div class="service">

                <span>OrganizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o</span>

                <span class="online">ONLINE</span>

            </div>



        </div>



        <div class="card">



            <div class="card-title">

                ALERTAS DA TORRE

            </div>



            <div class="alert">

                Nenhum alerta crÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tico detectado

            </div>



        </div>



    </div>



    <div class="center-panel">



        <div class="tower">



            <div class="center-title">

                TORRE EXECUTIVA GLOBAL

            </div>



            <div class="layers">



                <div class="layer">

                    <div class="layer-name">

                        PRESIDÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ NCIA

                    </div>



                    <div class="layer-status">

                        ONLINE

                    </div>

                </div>



                <div class="layer">

                    <div class="layer-name">

                        GOVERNANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡A

                    </div>



                    <div class="layer-status">

                        ONLINE

                    </div>

                </div>



                <div class="layer">

                    <div class="layer-name">

                        PRODUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

                    </div>



                    <div class="layer-status">

                        ONLINE

                    </div>

                </div>



                <div class="layer">

                    <div class="layer-name">

                        CURADORIA

                    </div>



                    <div class="layer-status">

                        ONLINE

                    </div>

                </div>



                <div class="layer">

                    <div class="layer-name">

                        CRIATIVIDADE

                    </div>



                    <div class="layer-status">

                        ONLINE

                    </div>

                </div>



                <div class="layer">

                    <div class="layer-name">

                        ORQUESTRAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

                    </div>



                    <div class="layer-status">

                        ONLINE

                    </div>

                </div>



            </div>



            <div class="footer">

                IOTEC EXECUTIVE VISUAL OPERATIONS CENTER

            </div>



        </div>



    </div>



    <div class="right-panel">



        <div class="card">



            <div class="card-title">

                EXECUTIVOS IA

            </div>



            <div class="executive">

                MASTER GOVERNANCE

            </div>



            <div class="executive">

                EXECUTIVE COMMAND

            </div>



            <div class="executive">

                ORCHESTRATOR ENGINE

            </div>



            <div class="executive">

                CREATIVE EXPLORER

            </div>



            <div class="executive">

                CONSOLIDATION ENGINE

            </div>



        </div>



        <div class="card">



            <div class="card-title">

                STATUS GLOBAL

            </div>



            <div class="service">

                <span>Ativos</span>

                <span>19455</span>

            </div>



            <div class="service">

                <span>Executivos</span>

                <span>20</span>

            </div>



            <div class="service">

                <span>CrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­ticos</span>

                <span>96</span>

            </div>



            <div class="service">

                <span>Institucionais</span>

                <span>247</span>

            </div>



        </div>



    </div>



</div>



</body>



</html>



"""



# =========================================================

# HOME

# =========================================================



@app.route('/')



def home():
    pass



    return HTML



# =========================================================

# START

# =========================================================



if __name__ == '__main__':
    pass



    print("")

    print("=" * 70)

    print(" IOTEC EXECUTIVE VISUAL OPERATIONS CENTER ")

    print("=" * 70)

    print("")



    app.run(



        host='0.0.0.0',



        port=7900

    )






