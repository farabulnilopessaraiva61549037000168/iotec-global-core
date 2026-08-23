import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import tkinter as tk
from tkinter import messagebox
import time

def abrir_sistema():
    status_var.set("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Acesso autorizado...")
    janela.update()
    time.sleep(1.5)
    messagebox.showinfo("Acesso", "Bem-vindo ao Comando FARABULINI.\nSistema desbloqueado.")
    status_var.set("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¢ Sistema operacional")

def sair():
    status_var.set("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Encerrando sistema...")
    janela.update()
    time.sleep(1)
    janela.destroy()

# Janela principal
janela = tk.Tk()
janela.title("CENTRAL DE COMANDO - FARABULINI AI")
janela.geometry("650x400")
janela.configure(bg="#0f0f0f")

# TÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tulo principal
titulo = tk.Label(janela, text="ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¸ CENTRAL DE COMANDO - FARABULINI",
                   fg="cyan", bg="#0f0f0f", font=("Consolas", 18, "bold"))
titulo.pack(pady=10)

# SubtÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tulo - domÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nio
sub = tk.Label(janela, text="ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  DOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNIO ABSOLUTO | PROPRIETÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO: FARABULINI LOPES SARAIVA - CPF: 011.902.313-01",
                 fg="lime", bg="#0f0f0f", font=("Consolas", 10))
sub.pack(pady=5)

# Caixa de status
status_var = tk.StringVar()
status_var.set("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¡ Aguardando comando...")

status = tk.Label(janela, textvariable=status_var,
                   fg="yellow", bg="#1a1a1a", width=60, height=2,
                   font=("Consolas", 10))
status.pack(pady=10)

# BotÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes de aÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
frame = tk.Frame(janela, bg="#0f0f0f")
frame.pack(pady=10)

bot_abrir = tk.Button(frame, text="ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ INICIAR SISTEMA", command=abrir_sistema,
                       bg="#004d00", fg="white", width=20, height=2,
                       font=("Consolas", 12, "bold"))
bot_abrir.grid(row=0, column=0, padx=10)

bot_sair = tk.Button(frame, text="ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ENCERRAR", command=sair,
                      bg="#800000", fg="white", width=20, height=2,
                      font=("Consolas", 12, "bold"))
bot_sair.grid(row=0, column=1, padx=10)

# Assinatura
assinatura = tk.Label(janela, text="Sistema protegido - DomÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nio absoluto de FARABULINI ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© 2025",
                       fg="gray", bg="#0f0f0f", font=("Consolas", 8))
assinatura.pack(side="bottom", pady=10)

janela.mainloop()



