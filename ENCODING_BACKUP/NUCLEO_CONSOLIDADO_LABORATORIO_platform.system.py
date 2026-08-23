import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import psutil
import platform
import datetime
import socket

def get_system_health():
    system_info = {
        "Sistema Operacional": platform.system(),
        "VersÃƒÆ'Ã†â€™o": platform.version(),
        "Nome do Host": socket.gethostname(),
        "Tempo de Atividade": str(datetime.timedelta(seconds=int(psutil.boot_time()))),
        "Uso de CPU (%)": psutil.cpu_percent(interval=1),
        "Uso de MemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria (%)": psutil.virtual_memory().percent,
        "Uso de Disco (%)": psutil.disk_usage('/').percent,
        "Total de RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        "IP Interno": socket.gethostbyname(socket.gethostname()),
        "Bytes Enviados": psutil.net_io_counters().bytes_sent,
        "Bytes Recebidos": psutil.net_io_counters().bytes_recv,
    }

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  SAÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡DE DO SISTEMA")
    print("-" * 40)
    for key, value in system_info.items():
        print(f"{key}: {value}")
    print("-" * 40)

get_system_health()



