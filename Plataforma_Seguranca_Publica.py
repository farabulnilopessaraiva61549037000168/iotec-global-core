import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# -*- coding: utf-8 -*-



import sys

import os

import random

import time

from collections import Counter



from PyQt5.QtWidgets import (

    QApplication, QMainWindow, QWidget, QVBoxLayout,

    QHBoxLayout, QLabel, QPushButton, QTextEdit, QComboBox

)

from PyQt5.QtCore import QTimer, QUrl

from PyQt5.QtWebEngineWidgets import QWebEngineView



import folium

from folium.plugins import HeatMap



# ==============================

# CONFIGURAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ==============================



DIRETORIO = "C:/IOTEC"

MAPA_INTERIOR = os.path.join(DIRETORIO, "mapa_interior.html")

MAPA_CAPITAL = os.path.join(DIRETORIO, "mapa_capital.html")



# ==============================

# REGIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES

# ==============================



REGIOES = {

    "SertÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Central": {

        "QuixadÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡": (-4.970, -39.015),

        "Quixeramobim": (-5.199, -39.290),

        "BanabuiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº": (-5.303, -38.920),

        "Ibaretama": (-4.803, -39.002),

        "ChorÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³": (-4.837, -39.139),

        "Ibicuitinga": (-4.969, -38.638)

    },

    "Vale do Jaguaribe": {

        "Limoeiro do Norte": (-5.145, -38.085),

        "Russas": (-4.940, -37.975),

        "Jaguaribe": (-5.890, -38.620),

        "Morada Nova": (-5.106, -38.370),

        "SÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o JoÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o do Jaguaribe": (-5.146, -38.100),

        "Jaguaruana": (-4.833, -37.781),

        "Tabuleiro do Norte": (-5.243, -38.128)

    },

    "RegiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Metropolitana": {

        "Fortaleza": (-3.7319, -38.5267),

        "Caucaia": (-3.7361, -38.6531),

        "MaracanaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº": (-3.8767, -38.6256),

        "EusÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©bio": (-3.8900, -38.4500),

        "Aquiraz": (-3.9022, -38.3890)

    }

}



# ==============================

# SISTEMA

# ==============================



class Sistema(QMainWindow):
    pass

    def __init__(self):
        pass

        super().__init__()



        self.setWindowTitle("IOTEC SENTINEL - Monitoramento Regional")

        self.setGeometry(100, 100, 1400, 900)



        self.regiao_atual = "SertÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Central"

        self.dados = []



        self.init_ui()

        self.iniciar()



    # ==========================

    # INTERFACE

    # ==========================



    def init_ui(self):
        pass

        central = QWidget()

        self.setCentralWidget(central)



        layout_principal = QHBoxLayout()



        # MENU LATERAL

        menu = QVBoxLayout()



        self.combo = QComboBox()

        self.combo.addItems(REGIOES.keys())

        self.combo.currentTextChanged.connect(self.mudar_regiao)



        btn_salvar = QPushButton("Abrir pasta do sistema")

        btn_salvar.clicked.connect(self.abrir_pasta)



        menu.addWidget(QLabel("RegiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o"))

        menu.addWidget(self.combo)

        menu.addWidget(btn_salvar)

        menu.addStretch()



        # CONTEÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡DO

        conteudo = QVBoxLayout()



        # MAPAS

        self.mapa_interior = QWebEngineView()

        self.mapa_capital = QWebEngineView()



        conteudo.addWidget(self.mapa_interior, 2)

        conteudo.addWidget(self.mapa_capital, 2)



        # ALERTAS

        self.alertas = QTextEdit()

        self.alertas.setReadOnly(True)



        # IA

        self.ia = QTextEdit()

        self.ia.setReadOnly(True)



        conteudo.addWidget(self.alertas)

        conteudo.addWidget(self.ia)



        layout_principal.addLayout(menu, 1)

        layout_principal.addLayout(conteudo, 4)



        central.setLayout(layout_principal)



    # ==========================

    # LÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"GICA

    # ==========================



    def gerar_ocorrencia(self):
        pass

        regiao = self.regiao_atual

        cidade = random.choice(list(REGIOES[regiao].keys()))



        return {

            "regiao": regiao,

            "cidade": cidade,

            "coords": REGIOES[regiao][cidade],

            "tipo": random.choice(["Roubo", "Furto", "Suspeita"]),

            "hora": time.strftime("%H:%M:%S")

        }



    def criar_mapa(self, dados, centro):
        pass

        mapa = folium.Map(

            location=centro,

            zoom_start=9,

            tiles="CartoDB positron"

        )



        HeatMap(

            [d["coords"] for d in dados],

            radius=12,

            blur=15,

            min_opacity=0.3

        ).add_to(mapa)



        for d in dados[-20:]:
            pass

            folium.CircleMarker(

                location=d["coords"],

                radius=6,

                color="red",

                fill=True,

                fill_opacity=0.7,

                popup=f"{d['tipo']} - {d['cidade']}"

            ).add_to(mapa)



        return mapa



    def atualizar_mapas(self):
        pass

        interior = [d for d in self.dados if d["regiao"] != "RegiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Metropolitana"]

        capital = [d for d in self.dados if d["regiao"] == "RegiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Metropolitana"]



        mapa1 = self.criar_mapa(interior, [-5.1, -38.7])

        mapa2 = self.criar_mapa(capital, [-3.8, -38.5])



        if not os.path.exists(DIRETORIO):
            pass

            os.makedirs(DIRETORIO)



        mapa1.save(MAPA_INTERIOR)

        mapa2.save(MAPA_CAPITAL)



        self.mapa_interior.load(QUrl.fromLocalFile(MAPA_INTERIOR))

        self.mapa_capital.load(QUrl.fromLocalFile(MAPA_CAPITAL))



    def analisar(self):
        pass

        cont = Counter([d["cidade"] for d in self.dados])

        if not cont:
            pass

            return ""



        cidade, qtd = cont.most_common(1)[0]

        return f"{cidade} apresenta maior concentraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de ocorrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncias."



    def atualizar(self):
        pass

        d = self.gerar_ocorrencia()

        self.dados.append(d)



        self.alertas.append(f"{d['tipo']} em {d['cidade']}")

        self.ia.setText(self.analisar())



        self.atualizar_mapas()



    def iniciar(self):
        pass

        self.timer = QTimer()

        self.timer.timeout.connect(self.atualizar)

        self.timer.start(3000)



    def mudar_regiao(self, texto):
        pass

        self.regiao_atual = texto

        self.dados.clear()

        self.alertas.clear()

        self.ia.clear()



    def abrir_pasta(self):
        pass

        os.startfile(DIRETORIO)



# ==============================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ==============================



if __name__ == "__main__":
    pass

    app = QApplication(sys.argv)

    janela = Sistema()

    janela.show()

    sys.exit(app.exec_())






