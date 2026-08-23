import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Senha Mestra Definida
SENHA_MESTRA = "J4GU4R2025"

class PainelJaguar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JAGUAR SYSTEMS - PAINEL DE COMANDO")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: black; color: lime;")

        self.tela_login()

    def tela_login(self):
        self.label = QLabel("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Digite a Senha Mestra:", self)
        self.label.setFont(QFont('Arial', 16))
        self.label.setGeometry(250, 100, 400, 50)

        self.input = QLineEdit(self)
        self.input.setGeometry(250, 160, 300, 40)
        self.input.setEchoMode(QLineEdit.Password)

        self.botao = QPushButton("ACESSAR", self)
        self.botao.setGeometry(310, 220, 180, 40)
        self.botao.clicked.connect(self.verificar_senha)
        self.botao.setStyleSheet("background-color: lime; color: black; font-weight: bold;")

    def verificar_senha(self):
        if self.input.text() == SENHA_MESTRA:
            self.tela_principal()
        else:
            QMessageBox.warning(self, "Acesso Negado", "Senha Incorreta. Acesso Restrito.")

    def tela_principal(self):
        self.label.hide()
        self.input.hide()
        self.botao.hide()

        titulo = QLabel("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  JAGUAR SYSTEMS ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â IA OPERACIONAL", self)
        titulo.setFont(QFont('Arial', 18))
        titulo.setGeometry(150, 20, 600, 50)
        titulo.setAlignment(Qt.AlignCenter)

        self.caixa_comando = QLineEdit(self)
        self.caixa_comando.setGeometry(150, 100, 500, 40)
        self.caixa_comando.setPlaceholderText("Digite um comando... Ex: abrir painel web")
        self.caixa_comando.returnPressed.connect(self.executar_comando)

        self.resposta = QLabel("", self)
        self.resposta.setGeometry(150, 160, 500, 250)
        self.resposta.setWordWrap(True)
        self.resposta.setFont(QFont('Arial', 14))

    def executar_comando(self):
        comando = self.caixa_comando.text().lower()

        if "abrir painel web" in comando:
            self.resposta.setText("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â Abrindo painel web no navegador...")
            import webbrowser
            webbrowser.open("http://127.0.0.1:5000")
        elif "status" in comando:
            self.resposta.setText("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Sistema operacional. Todas as funÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes estÃƒÆ'Ã†â€™o online.")
        elif "desligar" in comando:
            self.resposta.setText("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÂ¢Ã¢â€šÂ¬Ã‹Å" Encerrando Jaguar Systems...")
            sys.exit()
        else:
            self.resposta.setText(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Comando nÃƒÆ'Ã†â€™o reconhecido: {comando}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = PainelJaguar()
    janela.show()
    sys.exit(app.exec_())


