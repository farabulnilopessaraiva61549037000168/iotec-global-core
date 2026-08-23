import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
// Arquivo: EmergencyLayout.jsx

import { useState, useEffect } from "react";

export default function EmergencyLayout() {
  const [darkMode, setDarkMode] = useState(false);
  const [status, setStatus] = useState("Modo EmergÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Ativado");
  const [hora, setHora] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setHora(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const toggleMode = () => setDarkMode(!darkMode);

  return (
    <div className={`${darkMode ? "bg-black text-white" : "bg-white text-black"} min-h-screen transition-all`}>
      <header className="p-4 border-b flex justify-between items-center">
        <h1 className="text-xl font-bold">ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Painel de EmergÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia - Complexo IO</h1>
        <button
          onClick={toggleMode}
          className="px-4 py-1 border rounded hover:bg-gray-200 dark:hover:bg-gray-800"
        >
          {darkMode ? "Modo Claro" : "Modo Escuro"}
        </button>
      </header>

      <main className="p-6 space-y-4">
        <div className="bg-yellow-100 border-l-4 border-yellow-500 p-4 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-100">
          <strong>Status:</strong> {status}
        </div>

        <div className="flex flex-col sm:flex-row justify-between gap-4">
          <div className="p-4 bg-gray-100 dark:bg-gray-800 rounded shadow w-full sm:w-1/2">
            <h2 className="font-semibold text-lg">ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Comando Inteligente IO</h2>
            <p>Diga ou digite o que deseja acessar:</p>
            <input
              className="mt-2 w-full px-3 py-2 border rounded dark:bg-gray-900"
              placeholder="Ex: Acesso aos arquivos de dados"
            />
          </div>

          <div className="p-4 bg-gray-100 dark:bg-gray-800 rounded shadow w-full sm:w-1/2">
            <h2 className="font-semibold text-lg">ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° Tempo Real</h2>
            <p>{hora.toLocaleString("pt-BR")}</p>
          </div>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-4">
          {["ImportaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", "SeguranÃƒÆ'Ã†â€™a", "InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia IO", "Acessar Logs"].map((item, i) => (
            <button
              key={i}
              className="p-4 bg-blue-500 text-white rounded shadow hover:bg-blue-600"
            >
              {item}
            </button>
          ))}
        </div>
      </main>

      <footer className="p-4 text-center text-sm opacity-50 mt-6">
        Sistema Operacional IO ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· Modo de ContingÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© {new Date().getFullYear()}
      </footer>
    </div>
  );
}



