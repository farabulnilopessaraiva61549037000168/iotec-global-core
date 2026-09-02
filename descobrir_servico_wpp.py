import psutil, os

print('=== PROCESSOS NODE / WPPCONNECT ===')
for p in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        cmdline = p.info.get('cmdline') or []
        cmd = ' '.join(cmdline)
        name = p.info.get('name') or ''
        if 'node' in name.lower() or 'wppconnect' in cmd.lower():
            pid = p.info['pid']
            print(f'PID: {pid} | Cmd: {cmd}')
    except Exception as e:
        pass

print('\n=== ARQUIVOS JS DE WHATSAPP EM C:\\IOTEC ===')
for root, dirs, files in os.walk(r'C:\IOTEC'):
    if 'node_modules' in root:
        continue
    for f in files:
        f_lower = f.lower()
        if f_lower.endswith('.js') and ('wpp' in f_lower or 'whatsapp' in f_lower or 'server' in f_lower or 'app' in f_lower):
            print(os.path.join(root, f))
