import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import hashlib
import tkinter as tk
from tkinter import messagebox

# Criar janela principal
janela = tk.Tk()
janela.title("PAINEL DE CONTROLE")
janela.geometry("400x300")
janela.configure(bg="#202020")

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do botÃƒÆ'Ã†â€™o
def executar():
    messagebox.showinfo("STATUS", "Sistema Autorizado e Operacional ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦")

# TÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tulo
titulo = tk.Label(janela, text="ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â DNA-SISTEMA-ORIGINAL",
                   font=("Arial", 14, "bold"), bg="#202020", fg="white")
titulo.pack(pady=20)

# BotÃƒÆ'Ã†â€™o
botao = tk.Button(janela, text="Executar Sistema", command=executar,
                   bg="#00FFAA", fg="black", font=("Arial", 12, "bold"))
botao.pack(pady=10)

# Encerrar
botao_sair = tk.Button(janela, text="Sair", command=janela.destroy,
                        bg="#FF4040", fg="white", font=("Arial", 10))
botao_sair.pack(pady=10)

# Rodar a janela
janela.mainloop()



