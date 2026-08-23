import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# Specter Fortress ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Motor de Invisibilidade e Defesa Digital

import os
import socket
import requests
import threading
from cryptography.fernet import Fernet
from stem import Signal
from stem.control import Controller

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â GeraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de chave de criptografia
key = Fernet.generate_key()
cipher = Fernet(key)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â°ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para alterar IP (via TOR)
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='tor_password')
        controller.signal(Signal.NEWNYM)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â Proxy Tor
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de coleta stealth
def stealth_scraper(url):
    try:
        renew_tor_ip()
        response = requests.get(url, proxies=proxies, timeout=10)
        encrypted_data = cipher.encrypt(response.content)
        with open('data_encrypted.bin', 'ab') as file:
            file.write(encrypted_data + b'\n')
    except Exception as e:
        print(f"Erro: {e}")

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ ExecuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Paralela
targets = [
    "https://example.com",
    "https://anotherdomain.com",
    "https://targetdata.com"
]

threads = []

for url in targets:
    t = threading.Thread(target=stealth_scraper, args=(url,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â°ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Coleta concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da e dados criptografados.")

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° Defesa Ativa
def firewall_block(ip):
    os.system(f"iptables -A INPUT -s {ip} -j DROP")
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« IP bloqueado: {ip}")

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å"Ãƒâ€šÃ‚ÂÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Honeypot Simples
def start_honeypot(port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(5)
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Â¤ Honeypot ativo na porta {port}")
    while True:
        conn, addr = sock.accept()
        print(f"ConexÃƒÆ'Ã†â€™o capturada de {addr}")
        firewall_block(addr[0])
        conn.close()

# Ativar Honeypot
honeypot_thread = threading.Thread(target=start_honeypot)
honeypot_thread.start()


