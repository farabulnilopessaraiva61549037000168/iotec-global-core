$Builder = "C:\IOTEC\IOTEC_PLATFORM_BUILDER.py"

if (!(Test-Path $Builder)) {
    Write-Host ""
    Write-Host "ERRO: Builder não encontrado."
    exit
}

Write-Host ""
Write-Host "==============================================="
Write-Host " IOTEC BUILDER REPAIR"
Write-Host "==============================================="
Write-Host ""

# Backup

$Backup = "$Builder.bak"

Copy-Item $Builder $Backup -Force

Write-Host "[OK] Backup criado."

# Ler usando codificação ANSI

$Content = Get-Content $Builder -Encoding Default -Raw

# Corrigir caracteres mais comuns

$Content = $Content.Replace("VersÃ£o","Versão")
$Content = $Content.Replace("DiretÃ³rio","Diretório")
$Content = $Content.Replace("MÃ“DULOS","MÓDULOS")
$Content = $Content.Replace("CRIANDO DIRETÃ“RIOS","CRIANDO DIRETÓRIOS")
$Content = $Content.Replace("ConfiguraÃ§Ã£o","Configuração")
$Content = $Content.Replace("InformaÃ§Ã£o","Informação")
$Content = $Content.Replace("ConexÃ£o","Conexão")
$Content = $Content.Replace("ExecuÃ§Ã£o","Execução")

# Salvar em UTF-8

$Utf8 = New-Object System.Text.UTF8Encoding($false)

[System.IO.File]::WriteAllText(

    $Builder,

    $Content,

    $Utf8

)

Write-Host "[OK] Arquivo convertido para UTF-8."

# Verificar se a classe existe

$HasStructure = Select-String `
    -Path $Builder `
    -Pattern "class ProjectStructureEngine" `
    -Quiet

if($HasStructure){

    Write-Host "[OK] ProjectStructureEngine localizada."

}else{

    Write-Host "[ERRO] ProjectStructureEngine não encontrada."

}

Write-Host ""
Write-Host "==============================================="
Write-Host " FINALIZADO "
Write-Host "==============================================="