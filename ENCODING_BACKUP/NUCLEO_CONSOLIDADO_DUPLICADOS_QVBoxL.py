import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sys
import psutil
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont


# =========================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DA CHAVE
# =========================
CHAVE_SECRETA = "FARABULINI0119"


# =========================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ CLASSE LOGIN
# =========================
class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¸ Terminal de Acesso - Nave FARABULINI")
        self.setGeometry(500, 200, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        titulo = QLabel("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â INSERIR CHAVE DE ACESSO")
        titulo.setFont(QFont("Arial", 14))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.campo_chave = QLineEdit()
        self.campo_chave.setPlaceholderText("Digite sua chave secreta")
        self.campo_chave.setEchoMode(QLineEdit.EchoMode.Password)

        btn_entrar = QPushButton("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¸ Entrar na Nave")
        btn_entrar.clicked.connect(self.verificar_chave)

        layout.addWidget(titulo)
        layout.addWidget(self.campo_chave)
        layout.addWidget(btn_entrar)

        self.setLayout(layout)

    def verificar_chave(self):
        if self.campo_chave.text() == CHAVE_SECRETA:
            self.close()
            self.painel = PainelFuturista()
            self.painel.show()
        else:
            QMessageBox.critical(self, "Acesso Negado", "Chave incorreta! ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â«")


# =========================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å"Ãƒâ€šÃ‚Â¥ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â CLASSE DO PAINEL
# =========================
class PainelFuturista(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Painel de Controle FARABULINI")
        self.setGeometry(400, 150, 600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        titulo = QLabel("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¸ NAVE FARABULINI - PAINEL DE COMANDO")
        titulo.setFont(QFont("Arial", 16))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cpu_label = QLabel("CPU: 0%")
        self.cpu_label.setFont(QFont("Consolas", 14))

        self.memoria_label = QLabel("MemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria RAM: 0%")
        self.memoria_label.setFont(QFont("Consolas", 14))

        btn_abrir_pasta = QPushButton("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Abrir Pasta Documentos")
        btn_abrir_pasta.clicked.connect(self.abrir_pasta)

        btn_encerrar = QPushButton("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Encerrar Sistema")
        btn_encerrar.clicked.connect(self.encerrar)

        # Layout horizontal para botÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
        botoes = QHBoxLayout()
        botoes.addWidget(btn_abrir_pasta)
        botoes.addWidget(btn_encerrar)

        layout.addWidget(titulo)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.memoria_label)
        layout.addLayout(botoes)

        self.setLayout(layout)

        # Timer para atualizar monitoramento
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_monitoramento)
        self.timer.start(1000)  # Atualiza a cada 1 segundo

    def atualizar_monitoramento(self):
        cpu = psutil.cpu_percent()
        memoria = psutil.virtual_memory().percent

        self.cpu_label.setText(f"CPU: {cpu}%")
        self.memoria_label.setText(f"MemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria RAM: {memoria}%")

    def abrir_pasta(self):
        import os
        os.system('explorer .')

    def encerrar(self):
        self.close()


# =========================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ EXECUTANDO A NAVE
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = TelaLogin()
    login.show()
    sys.exit(app.exec())


