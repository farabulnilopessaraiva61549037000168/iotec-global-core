$ROOT = "C:\IOTEC"

Write-Host ""
Write-Host "====================================="
Write-Host "X27 SAFE BLOCK REPAIR"
Write-Host "====================================="
Write-Host ""

$corrigidos = 0

Get-ChildItem $ROOT -Filter *.py -Recurse | ForEach-Object {

    try {

        $arquivo = $_.FullName

        $linhas = Get-Content $arquivo

        $saida = New-Object System.Collections.ArrayList

        for ($i = 0; $i -lt $linhas.Count; $i++) {

            $linha = $linhas[$i]

            [void]$saida.Add($linha)

            $texto = $linha.Trim()

            $ehBloco = (
                $texto -match '^def\s+.*:\s*$'      -or
                $texto -match '^class\s+.*:\s*$'    -or
                $texto -match '^if\s+.*:\s*$'       -or
                $texto -match '^elif\s+.*:\s*$'     -or
                $texto -eq 'else:'                  -or
                $texto -eq 'try:'                   -or
                $texto -match '^except.*:\s*$'      -or
                $texto -eq 'finally:'               -or
                $texto -match '^for\s+.*:\s*$'      -or
                $texto -match '^while\s+.*:\s*$'    -or
                $texto -match '^with\s+.*:\s*$'
            )

            if ($ehBloco) {

                $proxima = ""

                if ($i + 1 -lt $linhas.Count) {
                    $proxima = $linhas[$i + 1]
                }

                $indentAtual = ($linha.Length - $linha.TrimStart().Length)

                $indentProxima = ($proxima.Length - $proxima.TrimStart().Length)

                if (
                    ($proxima.Trim() -eq "") -or
                    ($indentProxima -le $indentAtual)
                ) {

                    [void]$saida.Add((" " * ($indentAtual + 4)) + "pass")
                }
            }
        }

        Set-Content `
            -Path $arquivo `
            -Value $saida `
            -Encoding UTF8

        $corrigidos++

    }
    catch {

    }

}

Write-Host ""
Write-Host "ARQUIVOS PROCESSADOS :" $corrigidos
Write-Host ""
Write-Host "REPARO FINALIZADO"