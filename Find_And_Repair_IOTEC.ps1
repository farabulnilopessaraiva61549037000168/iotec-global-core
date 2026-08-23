Write-Host ""
Write-Host "===================================================="
Write-Host " IOTEC INTELLIGENT SCANNER"
Write-Host "===================================================="
Write-Host ""

# ======================================================
# SEARCH
# ======================================================

$targets = @(
    "Tecnologia",
    "OFICINA_IOTEC"
)

# ======================================================
# ALL DRIVES
# ======================================================

$drives = Get-PSDrive `
    -PSProvider FileSystem

foreach ($drive in $drives) {

    Write-Host ""
    Write-Host "[SCANNING DRIVE]"
    Write-Host $drive.Root

    foreach ($target in $targets) {

        $folders = Get-ChildItem `
            -Path $drive.Root `
            -Directory `
            -Recurse `
            -ErrorAction SilentlyContinue |

            Where-Object {

                $_.Name -eq $target
            }

        foreach ($folder in $folders) {

            Write-Host ""
            Write-Host "===================================================="
            Write-Host " TARGET FOUND"
            Write-Host "===================================================="

            Write-Host $folder.FullName

            # ==============================================
            # HTML FILES
            # ==============================================

            $htmlFiles = Get-ChildItem `
                -Path $folder.FullName `
                -Filter *.html `
                -Recurse `
                -ErrorAction SilentlyContinue

            foreach ($file in $htmlFiles) {

                Write-Host ""
                Write-Host "[FOUND HTML]"
                Write-Host $file.FullName
            }
        }
    }
}

Write-Host ""
Write-Host "===================================================="
Write-Host " SCAN COMPLETE"
Write-Host "===================================================="