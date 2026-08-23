$path = "C:\IOTEC\IOTEC_MASTER_CORE.py"
$backup = "C:\IOTEC\IOTEC_MASTER_CORE_BACKUP.py"

Write-Host "=== AUTO FIX MASTER CORE ==="

# 1. Backup
Copy-Item $path $backup -Force
Write-Host "Backup criado: $backup"

# 2. Ler conteúdo
$content = Get-Content $path -Raw

# 3. Corrigir import (caso exista import errado)
$content = $content -replace "import importlib", "import importlib.util`nimport importlib.machinery"

# 4. Substituir função safe_import inteira
$oldFunction = @'
def safe_import(module_path):
    try:
        module_name = os.path.splitext(os.path.basename(module_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        ACTIVE_MODULES.append(module_name)
        return module
    except Exception as e:
        print(f"[ERROR] Falha ao carregar {module_path}")
        print(e)
        return None
'@

$newFunction = @'
def safe_import(module_path):
    try:
        import importlib.util

        module_name = os.path.splitext(os.path.basename(module_path))[0]

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        ACTIVE_MODULES.append(module_name)
        return module

    except Exception as e:
        print(f"[ERROR] Falha ao carregar {module_path}")
        print(e)
        return None
'@

$content = $content -replace [regex]::Escape($oldFunction), $newFunction

# 5. Salvar arquivo corrigido
Set-Content -Path $path -Value $content -Encoding UTF8

Write-Host "=== CORREÇÃO FINALIZADA ==="
Write-Host "Agora execute:"
Write-Host "python IOTEC_MASTER_CORE.py"