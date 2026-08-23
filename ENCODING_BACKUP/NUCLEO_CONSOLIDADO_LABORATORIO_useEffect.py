import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import React, { useState, useEffect } from "react"; import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button"; import { Mic, Volume2, VolumeX, RefreshCw } from "lucide-react";

const panels = [ "AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de Dados", "PerÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cia Forense", "Ecossistema", "AgronegÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³cio", "Engenharia de Portos", "Arquitetura Inteligente", "Comando e Controle", "JustiÃƒÆ'Ã†â€™a e EficiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia", "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde e BiociÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia", "Cultura e Arte", ];

export default function PainelJaguar() { const [painelAtual, setPainelAtual] = useState(0); const [modoDescanso, setModoDescanso] = useState(false); const [somLigado, setSomLigado] = useState(true); const [comandoVoz, setComandoVoz] = useState(false);

useEffect(() => { let rotacao; if (modoDescanso) { rotacao = setInterval(() => { setPainelAtual((prev) => (prev + 1) % panels.length); }, 4000); } return () => clearInterval(rotacao); }, [modoDescanso]);

const ativarComandoVoz = () => { setComandoVoz(true); if ("webkitSpeechRecognition" in window) { const recognition = new webkitSpeechRecognition(); recognition.lang = "pt-BR"; recognition.start();

recognition.onresult = (event) => { const comando = event.results[0][0].transcript.toLowerCase(); if (comando.includes("voltar")) { setModoDescanso(false); } else if (comando.includes("dados")) { setPainelAtual(0); } else if (comando.includes("arquitetura")) { setPainelAtual(5); } else if



