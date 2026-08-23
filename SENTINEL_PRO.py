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

    QHBoxLayout, QLabel, QTextEdit, QComboBox

)

from PyQt5.QtCore import QTimer, QUrl

from PyQt5.QtWebEngineWidgets import QWebEngineView



import folium

from folium.plugins import HeatMap



BASE_DIR = "C:/IOTEC"

MAPA = os.path.join(BASE_DIR, "mapa.html")



REGIOES = {

    "Interior": {

        "QuixadÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡": (-4.970, -39.015),

        "Quixeramobim": (-5.199, -39.290),

        "Ibicuitinga": (-4.969, -38.638),

        "Morada Nova": (-5.106, -38.370),

        "Russas": (-4.940, -37.975),

        "Limoeiro do Norte": (-5.145, -38.085)

    },

    "Capital": {

        "Fortaleza": (-3.7319, -38.5267),

        "Caucaia": (-3.7361, -38.6531),

        "MaracanaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº": (-3.8767, -38.6256)

    }

}



TIPOS = ["OcorrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia registrada", "Atividade suspeita", "Monitoramento ativo"]



class Sistema(QMainWindow):
    pass

    def __init__(self):
        pass

        super().__init__()



        self.setWindowTitle("IOTEC SENTINEL - Centro de Monitoramento Operacional")

        self.setGeometry(100, 100, 1400, 900)



        self.setStyleSheet("""

            QMainWindow { background-color: #050a14; }

            QLabel { color: #e6f1ff; font-size: 13px; }

            QTextEdit {

                background-color: #0f172a;

                color: #e6f1ff;

                border: 1px solid #1f2937;

            }

            QComboBox {

                background-color: #0f172a;

                color: white;

            }

        """)



        self.regiao = "Interior"

        self.dados = []



        self.init_ui()

        self.iniciar()



    # UI

    def init_ui(self):
        pass

        central = QWidget()

        self.setCentralWidget(central)



        layout = QHBoxLayout()



        # MENU

        menu = QVBoxLayout()

        menu.addWidget(QLabel("RegiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de monitoramento"))



        self.combo = QComboBox()

        self.combo.addItems(REGIOES.keys())

        self.combo.currentTextChanged.connect(self.mudar_regiao)



        menu.addWidget(self.combo)

        menu.addStretch()



        # CONTEÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡DO

        conteudo = QVBoxLayout()



        conteudo.addWidget(QLabel("Mapa de Monitoramento Operacional"))



        self.mapa = QWebEngineView()

        conteudo.addWidget(self.mapa, 3)



        conteudo.addWidget(QLabel("SituaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o operacional"))

        self.status = QTextEdit()

        self.status.setReadOnly(True)

        conteudo.addWidget(self.status)



        conteudo.addWidget(QLabel("AnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica"))

        self.analise = QTextEdit()

        self.analise.setReadOnly(True)

        conteudo.addWidget(self.analise)



        layout.addLayout(menu, 1)

        layout.addLayout(conteudo, 4)



        central.setLayout(layout)



    # LÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"GICA

    def gerar(self):
        pass

        cidade = random.choice(list(REGIOES[self.regiao].keys()))

        return {

            "cidade": cidade,

            "coords": REGIOES[self.regiao][cidade],

            "tipo": random.choice(TIPOS),

            "hora": time.strftime("%H:%M:%S")

        }



    def criar_mapa(self):
        pass

        mapa = folium.Map(

            location=[-5.0, -38.7],

            zoom_start=10,

            tiles="CartoDB dark_matter",

            control_scale=True

        )



        # HEATMAP

        HeatMap(

            [d["coords"] for d in self.dados],

            radius=12,

            blur=18,

            min_opacity=0.25

        ).add_to(mapa)



        # CAMADA TÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂTICA (visual forte)

        for d in self.dados[-20:]:
            pass

            folium.CircleMarker(

                location=d["coords"],

                radius=10,

                color="#00e5ff",

                fill=True,

                fill_opacity=0.2

            ).add_to(mapa)



        # MARCADORES PRINCIPAIS

        for d in self.dados[-10:]:
            pass

            folium.CircleMarker(

                location=d["coords"],

                radius=5,

                color="#00e5ff",

                fill=True,

                fill_opacity=0.9,

                popup=f"{d['tipo']} - {d['cidade']} - {d['hora']}"

            ).add_to(mapa)



        return mapa



    def atualizar_mapa(self):
        pass

        mapa = self.criar_mapa()



        if not os.path.exists(BASE_DIR):
            pass

            os.makedirs(BASE_DIR)



        mapa.save(MAPA)

        self.mapa.load(QUrl.fromLocalFile(MAPA))



    def analisar(self):
        pass

        if not self.dados:
            pass

            return ""



        cont = Counter([d["cidade"] for d in self.dados])

        cidade, qtd = cont.most_common(1)[0]



        return (

            f"RegiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o crÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tica identificada: {cidade}.\n"

            f"Volume elevado de registros recentes.\n"

            f"AÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o recomendada: monitoramento intensivo."

        )



    def atualizar(self):
        pass

        d = self.gerar()

        self.dados.append(d)



        self.status.append(

            f"[{d['hora']}] {d['tipo']} | {d['cidade']}"

        )



        # limpa excesso

        if self.status.document().blockCount() > 20:
            pass

            self.status.clear()



        self.analise.setText(self.analisar())



        self.atualizar_mapa()



    def iniciar(self):
        pass

        self.timer = QTimer()

        self.timer.timeout.connect(self.atualizar)

        self.timer.start(3000)



    def mudar_regiao(self, r):
        pass

        self.regiao = r

        self.dados.clear()

        self.status.clear()

        self.analise.clear()



# RUN

if __name__ == "__main__":
    pass

    app = QApplication(sys.argv)

    s = Sistema()

    s.show()

    sys.exit(app.exec_())






