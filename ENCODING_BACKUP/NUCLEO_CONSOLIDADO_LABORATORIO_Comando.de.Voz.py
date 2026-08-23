import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
// ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ESTE ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° O CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDIGO QUE DEVE SER COPIADO PARA O APP DA SIGMA // VERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: PAINEL JAGUAR INTERATIVO ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ REACT + COMANDO DE VOZ + CONTROLE DINÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡MICO

import React, { useState, useEffect } from 'react';

const paineis = [ 'AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de Dados', 'PerÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cia Forense', 'Engenharia de Portos', 'Ecossistemas', 'Arquitetura', 'AgronegÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³cio', 'JustiÃƒÆ'Ã†â€™a e EficiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia', 'Cultura e Arte' ];

export default function PainelJaguar() { const [painelAtual, setPainelAtual] = useState(0); const [modoDescanso, setModoDescanso] = useState(true); const [somAtivo, setSomAtivo] = useState(false); const [vozAtiva, setVozAtiva] = useState(false); const [toques, setToques] = useState(0);

useEffect(() => { let interval; if (modoDescanso) { interval = setInterval(() => { setPainelAtual((prev) => (prev + 1) % paineis.length); }, 5000); } return () => clearInterval(interval); }, [modoDescanso]);

useEffect(() => { if (vozAtiva && 'webkitSpeechRecognition' in window) { const recognition = new window.webkitSpeechRecognition(); recognition.continuous = true; recognition.lang = 'pt-BR'; recognition.onresult = (event) => { const comando = event.results[event.results.length - 1][0].transcript.toLowerCase(); console.log('Comando de voz:', comando); if (comando.includes('voltar')) { setModoDescanso(false); } else { const idx = paineis.findIndex(p => comando.includes(p.toLowerCase())); if (idx !== -1) { setPainelAtual(idx); setModoDescanso(false); } } }; recognition.start(); return () => recognition.stop(); } }, [vozAtiva]);

const aoClicarPainel = () => { setModoDescanso(false); };

const aoDuploToque = () => { setModoDescanso(false); setPainelAtual(0); };

const registrarToque



