$builder = "C:\IOTEC\IOTEC_PLATFORM_BUILDER.py"

if (!(Test-Path $builder)) {
    Write-Host ""
    Write-Host "ERRO: IOTEC_PLATFORM_BUILDER.py não encontrado."
    exit
}

$codigo = @'

# =============================================================================
# PROJECT STRUCTURE ENGINE
# =============================================================================

class ProjectStructureEngine:

    def __init__(self, kernel):

        self.kernel = kernel

        self.directories = [

            "core",
            "kernel",
            "modules",
            "agents",
            "commercial",
            "contracts",
            "crm",
            "finance",
            "gateway",
            "connectors",
            "security",
            "audit",
            "database",
            "config",
            "plugins",
            "logs",
            "reports",
            "dashboard",
            "scheduler",
            "services",
            "storage",
            "warroom",
            "temp",
            "tests"

        ]

    def create_directories(self):

        print()
        print("="*90)
        print("CRIANDO DIRETÓRIOS")
        print("="*90)

        for directory in self.directories:

            folder = PROJECT_ROOT / directory

            folder.mkdir(
                parents=True,
                exist_ok=True
            )

            print(f"[ OK ] {directory}")

        print()
        print("ESTRUTURA CRIADA.")
        print()

'@

Add-Content -Path $builder -Value $codigo

Write-Host ""
Write-Host "==========================================="
Write-Host "ETAPA 02 APLICADA COM SUCESSO"
Write-Host "==========================================="
Write-Host ""