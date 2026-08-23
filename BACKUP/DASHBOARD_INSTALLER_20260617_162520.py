import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC DASHBOARD INSTALLER

# AUTOMACAO TOTAL DO FRONTEND OPERACIONAL

# =========================================================



Write-Host ""

Write-Host "==================================================" -ForegroundColor Cyan

Write-Host " IOTEC CENTRAL OPERACIONAL INSTALLER " -ForegroundColor Cyan

Write-Host "==================================================" -ForegroundColor Cyan

Write-Host ""



# =========================================================

# VERIFICAR NODE

# =========================================================



Write-Host "[1/8] VERIFICANDO NODE.JS..." -ForegroundColor Yellow



$node = node -v 2>$null



if (!$node) {



    Write-Host ""

    Write-Host "NODE.JS NAO ENCONTRADO" -ForegroundColor Red

    Write-Host ""

    Write-Host "BAIXE EM:"

    Write-Host "https://nodejs.org"

    Write-Host ""



    pause

    exit

}



Write-Host "NODE DETECTADO: $node" -ForegroundColor Green



# =========================================================

# PASTA

# =========================================================



Write-Host ""

Write-Host "[2/8] PREPARANDO PASTA..." -ForegroundColor Yellow



$PASTA = "C:\IOTEC_DASHBOARD"



if (!(Test-Path $PASTA)) {



    New-Item `

        -ItemType Directory `

        -Path $PASTA | Out-Null

}



Set-Location $PASTA



Write-Host "PASTA OK" -ForegroundColor Green



# =========================================================

# CRIAR VITE

# =========================================================



Write-Host ""

Write-Host "[3/8] CRIANDO FRONTEND REACT..." -ForegroundColor Yellow



npm create vite@latest . -- --template react



# =========================================================

# INSTALL

# =========================================================



Write-Host ""

Write-Host "[4/8] INSTALANDO DEPENDENCIAS..." -ForegroundColor Yellow



npm install



# =========================================================

# TAILWIND

# =========================================================



Write-Host ""

Write-Host "[5/8] INSTALANDO TAILWIND..." -ForegroundColor Yellow



npm install -D tailwindcss postcss autoprefixer



npx tailwindcss init -p



# =========================================================

# CONFIG TAILWIND

# =========================================================



Write-Host ""

Write-Host "[6/8] CONFIGURANDO TAILWIND..." -ForegroundColor Yellow



@"

module.exports = {



  content: [



    "./index.html",



    "./src/**/*.{js,ts,jsx,tsx}"

  ],



  theme: {



    extend: {},

  },



  plugins: [],

}

"@ | Set-Content "tailwind.config.js"



@"

@tailwind base;

@tailwind components;

@tailwind utilities;



body {



    margin: 0;

    padding: 0;

    overflow: hidden;

    background: black;

}

"@ | Set-Content "src\index.css"



# =========================================================

# APP JSX

# =========================================================



Write-Host ""

Write-Host "[7/8] CRIANDO CENTRAL OPERACIONAL..." -ForegroundColor Yellow



@"

export default function App() {



  return (



    <div className='w-screen h-screen bg-black text-cyan-400 flex items-center justify-center'>



      <div className='text-center'>



        <h1 className='text-6xl font-bold tracking-widest'>



          IOTEC CENTRAL OPERACIONAL



        </h1>



        <p className='mt-6 text-xl text-cyan-200'>



          Infraestrutura Modular Supervisada



        </p>



        <div className='mt-10 w-6 h-6 rounded-full bg-green-400 animate-pulse mx-auto shadow-[0_0_25px_#00ff88]' />



      </div>



    </div>

  )

}

"@ | Set-Content "src\App.jsx"



# =========================================================

# RODAR

# =========================================================



Write-Host ""

Write-Host "[8/8] INICIANDO DASHBOARD..." -ForegroundColor Yellow

Write-Host ""



npm run dev





