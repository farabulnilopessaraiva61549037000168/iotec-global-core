import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
print('=' * 40)
print(' GLOBAL ORCHESTRATOR ONLINE ')
print('=' * 40)

print('')
print('[OK] Registry Core Loaded')
print('[OK] Port Scanner Loaded')
print('[OK] Premium Environment Ready')
print('')

input('Press ENTER to keep alive...')


