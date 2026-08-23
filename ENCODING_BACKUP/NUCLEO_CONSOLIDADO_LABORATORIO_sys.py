import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sys
import psutil
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox, QLineEdit
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

# ====== ConfiguraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o da Chave de Acesso ======
CHAVE_ACESSO = "FARABULINI2025"

# ====== Janela Principal ======
class PainelFuturista(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NAVE-MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢E FARABULINI - Painel de Controle")
        self.setGeometry(200, 200, 500, 400)
        self.setStyleSheet("background-color: #0d0d0d; color: #00ffff;")
        self.initUI()

    def initUI(self):
        fonte = QFont('Consolas', 12)

        self.label_status = QLabel("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Sistema Seguro Ativado")
        self.label_status.setFont(fonte)

        self.cpu_label = QLabel("CPU: ")
        self.cpu_label.setFont(fonte)

        self.ram_label = QLabel("RAM: ")
        self.ram_label.setFont(fonte)

        # BotÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes de comandos
        btn_abrir_pasta = QPushButton("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Abrir Pasta")
        btn_executar = QPushButton("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Executar Comando")
        btn_sair = QPushButton("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Encerrar Sistema")

        btn_abrir_pasta.clicked.connect(self.abrir_pasta)
        btn_executar.clicked.connect(self.executar_comando)
        btn_sair.clicked.connect(self.close)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_status)
        vbox.addWidget(self.cpu_label)
        vbox.addWidget(self.ram_label)

        hbox = QHBoxLayout()
        hbox.addWidget(btn_abrir_pasta)
        hbox.addWidget(btn_executar)
        hbox.addWidget(btn_sair)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # Timer para atualizar o status da mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡quina
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_status)
        self.timer.start(1000)

    def atualizar_status(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        self.cpu_label.setText(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å"Ãƒâ€šÃ‚Â¥ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â CPU Uso: {cpu}%")
        self.ram_label.setText(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â¾ RAM Uso: {ram}%")

    def abrir_pasta(self):
        QMessageBox.information(self, "Abrir Pasta", "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de abrir pasta acionada!")

    def executar_comando(self):
        QMessageBox.information(self, "Executar", "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â°ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de executar comando acionada!")

# ====== Tela de Login com Chave de Acesso ======
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Âª Acesso Restrito - NAVE FARABULINI")
        self.setGeometry(300, 300, 400, 200)
        self.setStyleSheet("background-color: black; color: #00ffcc;")
        self.initUI()

    def initUI(self):
        fonte = QFont('Consolas', 11)

        self.label = QLabel("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Digite sua CHAVE DE ACESSO:")
        self.label.setFont(fonte)

        self.input = QLineEdit()
        self.input.setEchoMode(QLineEdit.EchoMode.Password)
        self.input.setFont(fonte)

        self.botao = QPushButton("Entrar")
        self.botao.clicked.connect(self.verificar)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.input)
        vbox.addWidget(self.botao)

        self.setLayout(vbox)

    def verificar(self):
        if self.input.text() == CHAVE_ACESSO:
            self.close()
            self.painel = PainelFuturista()
            self.painel.show()
        else:
            QMessageBox.warning(self, "Acesso Negado", "ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Chave incorreta. Acesso bloqueado.")

# ====== Rodar Programa ======
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())


