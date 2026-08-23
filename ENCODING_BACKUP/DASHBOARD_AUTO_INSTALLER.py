import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC DASHBOARD AUTO INSTALLER
# PYTHON VERSION
# =========================================================

import os
import subprocess
import sys

# =========================================================
# EXECUTOR
# =========================================================

def executar(comando):
    pass

    print("")
    print(f">>> {comando}")
    print("")

    subprocess.run(

        comando,

        shell=True
    )

# =========================================================
# HEADER
# =========================================================

print("")
print("=" * 60)
print(" IOTEC CENTRAL OPERACIONAL INSTALLER ")
print("=" * 60)
print("")

# =========================================================
# VERIFICAR NODE
# =========================================================

print("[1/7] VERIFICANDO NODE...")

try:
    pass

    resultado = subprocess.check_output(

        "node -v",

        shell=True,

        text=True
    )

    print(f"NODE DETECTADO: {resultado}")

except:
    pass

    print("")
    print("NODE.JS NAO ENCONTRADO")
    print("")
    print("BAIXE EM:")
    print("https://nodejs.org")
    print("")

    sys.exit()

# =========================================================
# PASTA
# =========================================================

print("[2/7] PREPARANDO PASTA...")

PASTA = r"C:\IOTEC_DASHBOARD"

if not os.path.exists(PASTA):
    pass

    os.makedirs(PASTA)

os.chdir(PASTA)

print(f"PASTA: {PASTA}")

# =========================================================
# VITE
# =========================================================

print("[3/7] CRIANDO PROJETO REACT...")

executar(

    "npm create vite@latest . -- --template react"
)

# =========================================================
# INSTALL
# =========================================================

print("[4/7] INSTALANDO DEPENDENCIAS...")

executar(

    "npm install"
)

# =========================================================
# TAILWIND
# =========================================================

print("[5/7] INSTALANDO TAILWIND...")

executar(

    "npm install -D tailwindcss postcss autoprefixer"
)

executar(

    "npx tailwindcss init -p"
)

# =========================================================
# TAILWIND CONFIG
# =========================================================

print("[6/7] CONFIGURANDO TAILWIND...")

tailwind = '''
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
'''

with open(

    "tailwind.config.js",

    "w",

    encoding="utf-8"

) as f:

    f.write(tailwind)

css = '''
@tailwind base;
@tailwind components;
@tailwind utilities;

body {

    margin: 0;
    padding: 0;
    overflow: hidden;
    background: black;
}
'''

with open(

    r"src\\index.css",

    "w",

    encoding="utf-8"

) as f:

    f.write(css)

# =========================================================
# APP JSX
# =========================================================

print("[7/7] CRIANDO DASHBOARD...")

appjsx = r'''
export default function App() {

  return (

    <div className="w-screen h-screen bg-black text-cyan-400 flex items-center justify-center">

      <div className="text-center">

        <h1 className="text-6xl font-bold tracking-widest">

          IOTEC CENTRAL OPERACIONAL

        </h1>

        <p className="mt-6 text-xl text-cyan-200">

          Infraestrutura Modular Supervisada

        </p>

        <div className="mt-10 w-6 h-6 rounded-full bg-green-400 animate-pulse mx-auto shadow-[0_0_25px_#00ff88]" />

      </div>

    </div>
  )
}
'''

with open(

    r"src\\App.jsx",

    "w",

    encoding="utf-8"

) as f:

    f.write(appjsx)

# =========================================================
# FINAL
# =========================================================

print("")
print("=" * 60)
print(" DASHBOARD CRIADO COM SUCESSO ")
print("=" * 60)
print("")

print("PASTA:")
print(PASTA)
print("")

print("EXECUTE:")
print("")
print("cd C:\\IOTEC_DASHBOARD")
print("npm run dev")
print("")

print("URL:")
print("http://localhost:5173")
print("")


