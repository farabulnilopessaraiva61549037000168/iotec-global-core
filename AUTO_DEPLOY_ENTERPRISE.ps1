# AUTO_DEPLOY_ENTERPRISE.ps1

Write-Host ""
Write-Host "================================================"
Write-Host " GLOBAL ENTERPRISE INTELLIGENCE "
Write-Host " AUTO DEPLOY ENGINE "
Write-Host "================================================"
Write-Host ""

# ============================================================
# CHECK PYTHON
# ============================================================

Write-Host "[1/10] CHECKING PYTHON..."

python --version

# ============================================================
# CHECK GIT
# ============================================================

Write-Host ""
Write-Host "[2/10] CHECKING GIT..."

git --version

# ============================================================
# CREATE REQUIREMENTS
# ============================================================

Write-Host ""
Write-Host "[3/10] CREATING requirements.txt..."

@"
flask
gunicorn
requests
"@ | Set-Content requirements.txt

# ============================================================
# CREATE PROCFILE
# ============================================================

Write-Host ""
Write-Host "[4/10] CREATING Procfile..."

@"
web: gunicorn ENTERPRISE_RENDER_READY:app
"@ | Set-Content Procfile

# ============================================================
# CREATE .GITIGNORE
# ============================================================

Write-Host ""
Write-Host "[5/10] CREATING .gitignore..."

@"
__pycache__/
*.pyc
enterprise.db
"@ | Set-Content .gitignore

# ============================================================
# INSTALL PACKAGES
# ============================================================

Write-Host ""
Write-Host "[6/10] INSTALLING PACKAGES..."

pip install flask
pip install gunicorn
pip install requests

# ============================================================
# GIT INIT
# ============================================================

Write-Host ""
Write-Host "[7/10] INITIALIZING GIT..."

git init

# ============================================================
# GIT ADD
# ============================================================

Write-Host ""
Write-Host "[8/10] ADDING FILES..."

git add .

# ============================================================
# GIT COMMIT
# ============================================================

Write-Host ""
Write-Host "[9/10] CREATING COMMIT..."

git commit -m "GLOBAL ENTERPRISE INTELLIGENCE ONLINE"

# ============================================================
# LOCAL START
# ============================================================

Write-Host ""
Write-Host "[10/10] STARTING ENTERPRISE SYSTEM..."

Start-Process powershell -ArgumentList "python ENTERPRISE_RENDER_READY.py"

Write-Host ""
Write-Host "================================================"
Write-Host " ENTERPRISE SYSTEM ONLINE "
Write-Host "================================================"
Write-Host ""
Write-Host "LOCAL:"
Write-Host "http://127.0.0.1:3000"
Write-Host ""
Write-Host "NEXT STEP:"
Write-Host "1 - CREATE GITHUB REPOSITORY"
Write-Host "2 - git remote add origin YOUR_REPOSITORY"
Write-Host "3 - git push -u origin main"
Write-Host "4 - CONNECT TO RENDER"
Write-Host ""
Write-Host "================================================"
Write-Host ""