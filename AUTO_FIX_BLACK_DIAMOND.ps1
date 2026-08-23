Write-Host ""
Write-Host "====================================="
Write-Host " BLACK DIAMOND AUTO FIX"
Write-Host "====================================="
Write-Host ""

Set-Location "C:\IOTEC\black-diamond"

Write-Host "[1/5] Instalando dependencias..."
npm install tailwindcss postcss autoprefixer

Write-Host "[2/5] Criando tailwind.config.js..."

@"
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
"@ | Set-Content tailwind.config.js

Write-Host "[3/5] Criando postcss.config.js..."

@"
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"@ | Set-Content postcss.config.js

Write-Host "[4/5] Corrigindo src/index.css..."

@"
@tailwind base;
@tailwind components;
@tailwind utilities;

html,
body,
#root {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: black;
  overflow: hidden;
  font-family: Inter, sans-serif;
}
"@ | Set-Content src/index.css

Write-Host "[5/5] Iniciando servidor..."

npm run dev