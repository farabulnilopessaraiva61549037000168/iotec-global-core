import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==============================

# IOTEC SENTINEL - NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEL MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂXIMO REGIONAL (VERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O PROFISSIONAL)

# ==============================



import sys

import os

import random

import time

from collections import Counter



from PyQt5.QtWidgets import (

    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,

    QLabel, QPushButton, QTextEdit, QFrame, QScrollArea

)

from PyQt5.QtCore import Qt, QTimer, QUrl

from PyQt5.QtGui import QFont

from PyQt5.QtWebEngineWidgets import QWebEngineView



import folium

from folium.plugins import HeatMap



APP_NAME = "IOTEC SENTINEL"

CNPJ = "61.549.037/0001-68"

DIRETORIO = "C:/IOTEC"

MAP_FILE = os.path.join(DIRETORIO, "mapa.html")



# ==============================

# ESTRUTURA REGIONAL

# ==============================



REGIAO = {

    "Vale do Jaguaribe": {

        "SÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o JoÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o do Jaguaribe": {

            "Centro": (-5.146, -38.100),

            "Lagoa Grande": (-5.155, -38.120)

        },

        "Limoeiro do Norte": {

            "Centro": (-5.145, -38.085),

            "Bom Nome": (-5.150, -38.090)

        }

    },

    "SertÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Central": {

        "QuixadÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡": {

            "Centro": (-4.970, -39.015),

            "Campo Velho": (-4.975, -39.020)

        },

        "Quixeramobim": {

            "Centro": (-5.199, -39.290),

            "Maravilha": (-5.205, -39.295)

        }

    }

}



class PainelPrincipal(QMainWindow):
    pass

    def __init__(self):
        pass

        super().__init__()

        self.setWindowTitle(f"{APP_NAME} - Monitoramento Regional")

        self.setGeometry(100, 100, 1400, 900)



        self.setStyleSheet("""

            QMainWindow { background-color: #0a0f1a; }

            QLabel { color: #e6f1ff; }

            QPushButton {

                background-color: #112240;

                color: #64ffda;

                border: 1px solid #64ffda;

                padding: 8px;

                border-radius: 6px;

            }

            QPushButton:hover { background-color: #1f4068; }

        """)



        self.dados = []

        self.init_ui()

        self.simular_dados()



    def init_ui(self):
        pass

        central = QWidget()

        self.setCentralWidget(central)



        layout_principal = QHBoxLayout()



        sidebar = QVBoxLayout()

        sidebar_label = QLabel("MENU OPERACIONAL")

        sidebar_label.setFont(QFont("Arial", 12, QFont.Bold))



        btn_simular = QPushButton("INICIAR OCORRÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ NCIA")

        btn_simular.clicked.connect(self.iniciar_ocorrencia)



        sidebar.addWidget(sidebar_label)

        sidebar.addWidget(btn_simular)

        sidebar.addStretch()



        conteudo = QVBoxLayout()



        header = QHBoxLayout()

        titulo = QLabel(f"{APP_NAME} | Monitoramento Regional | CNPJ: {CNPJ}")

        titulo.setFont(QFont("Arial", 16, QFont.Bold))



        self.status = QLabel("STATUS: ONLINE | IA REGIONAL ATIVA")



        header.addWidget(titulo)

        header.addStretch()

        header.addWidget(self.status)



        conteudo.addLayout(header)



        self.mapa_view = QWebEngineView()

        conteudo.addWidget(self.mapa_view, 2)



        scroll = QScrollArea()

        scroll.setWidgetResizable(True)



        container = QWidget()

        self.layout_conteudo = QVBoxLayout(container)



        self.alertas = self.criar_modulo("ALERTAS EM TEMPO REAL")

        self.risco = self.criar_modulo("ANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLISE DE RISCO REGIONAL")

        self.ia = self.criar_modulo("ASSISTENTE INTELIGENTE")



        self.layout_conteudo.addWidget(self.alertas)

        self.layout_conteudo.addWidget(self.risco)

        self.layout_conteudo.addWidget(self.ia)



        scroll.setWidget(container)

        conteudo.addWidget(scroll, 3)



        layout_principal.addLayout(sidebar, 1)

        layout_principal.addLayout(conteudo, 4)



        central.setLayout(layout_principal)



    def criar_modulo(self, titulo_texto):
        pass

        frame = QFrame()

        frame.setStyleSheet("background-color: #112240; border-radius: 8px;")

        layout = QVBoxLayout()



        titulo = QLabel(titulo_texto)

        titulo.setFont(QFont("Arial", 12, QFont.Bold))



        conteudo = QTextEdit()

        conteudo.setReadOnly(True)

        conteudo.setStyleSheet("background-color: #0a192f; color: #ccd6f6;")



        layout.addWidget(titulo)

        layout.addWidget(conteudo)

        frame.setLayout(layout)



        frame.texto = conteudo

        return frame



    def simular_dados(self):
        pass

        self.timer = QTimer()

        self.timer.timeout.connect(self.atualizar_dados)

        self.timer.start(2000)



    def gerar_ocorrencia(self):
        pass

        regiao = random.choice(list(REGIAO.keys()))

        cidade = random.choice(list(REGIAO[regiao].keys()))

        bairro = random.choice(list(REGIAO[regiao][cidade].keys()))



        coords = REGIAO[regiao][cidade][bairro]

        tipo = random.choice(["Roubo", "Furto", "Suspeita"])



        ocorrencia = {

            "regiao": regiao,

            "cidade": cidade,

            "bairro": bairro,

            "coords": coords,

            "tipo": tipo,

            "hora": time.strftime("%H:%M:%S")

        }



        self.dados.append(ocorrencia)

        return ocorrencia



    def atualizar_mapa(self):
        pass

        mapa = folium.Map(location=[-5.0, -38.5], zoom_start=8)



        heat_data = [d["coords"] for d in self.dados]

        HeatMap(heat_data, radius=18).add_to(mapa)



        for d in self.dados[-30:]:
            pass

            folium.Marker(

                location=d["coords"],

                popup=f"{d['tipo']} - {d['bairro']} ({d['cidade']})"

            ).add_to(mapa)



        if not os.path.exists(DIRETORIO):
            pass

            os.makedirs(DIRETORIO)



        mapa.save(MAP_FILE)

        self.mapa_view.load(QUrl.fromLocalFile(MAP_FILE))



    def calcular_risco(self):
        pass

        contagem = Counter([d["cidade"] for d in self.dados])

        resultado = []



        for cidade, qtd in contagem.items():
            pass

            if qtd >= 8:
                pass

                nivel = "ALTO"

            elif qtd >= 4:
                pass

                nivel = "MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°DIO"

            else:
                pass

                nivel = "BAIXO"



            resultado.append((cidade, nivel, qtd))



        return resultado



    def gerar_mensagem_ia(self, top):
        pass

        frases = [

            f"A cidade de {top[0]} apresenta {top[2]} ocorrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncias recentes. AtenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o reforÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ada recomendada.",

            f"Detectado aumento de ocorrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncias em {top[0]}. Avaliar reforÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o operacional imediato.",

            f"PadrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de incidÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia identificado em {top[0]} com {top[2]} registros recentes.",

        ]

        return random.choice(frases)



    def atualizar_dados(self):
        pass

        ocorrencia = self.gerar_ocorrencia()



        self.alertas.texto.append(

            f"[{ocorrencia['hora']}] {ocorrencia['tipo']} no bairro {ocorrencia['bairro']} - {ocorrencia['cidade']} ({ocorrencia['regiao']})"

        )



        riscos = self.calcular_risco()

        self.risco.texto.clear()



        for cidade, nivel, qtd in riscos:
            pass

            simbolo = "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´" if nivel == "ALTO" else "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡" if nivel == "MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°DIO" else "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢"

            self.risco.texto.append(f"{simbolo} {cidade}: {nivel} ({qtd} ocorrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncias)")



        if riscos:
            pass

            top = max(riscos, key=lambda x: x[2])

            self.ia.texto.append(self.gerar_mensagem_ia(top))



        self.atualizar_mapa()



    def iniciar_ocorrencia(self):
        pass

        self.alertas.texto.append("=== OPERAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O INICIADA ===")

        self.ia.texto.append("Sistema intensificando monitoramento regional.")



if __name__ == "__main__":
    pass

    app = QApplication(sys.argv)

    janela = PainelPrincipal()

    janela.show()

    sys.exit(app.exec_())






