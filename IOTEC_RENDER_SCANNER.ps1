Write-Host ""
Write-Host "================================="
Write-Host "IOTEC RENDER SCANNER"
Write-Host "================================="

$url = "https://iotec-platform-1.onrender.com"

$rotas = @(
    "",
    "/",
    "/status",
    "/health",
    "/api",
    "/lead",
    "/leads",
    "/form",
    "/contact",
    "/dashboard",
    "/admin"
)

foreach($rota in $rotas)
{
    $alvo = $url + $rota

    Write-Host ""
    Write-Host "TESTANDO:"
    Write-Host $alvo

    try
    {
        $resposta = Invoke-WebRequest `
            -Uri $alvo `
            -Method GET `
            -TimeoutSec 20

        Write-Host "STATUS:" $resposta.StatusCode
    }
    catch
    {
        if($_.Exception.Response)
        {
            Write-Host "STATUS:" `
            $_.Exception.Response.StatusCode.value__
        }
        else
        {
            Write-Host "FALHA"
        }
    }
}

Write-Host ""
Write-Host "SCAN FINALIZADO"