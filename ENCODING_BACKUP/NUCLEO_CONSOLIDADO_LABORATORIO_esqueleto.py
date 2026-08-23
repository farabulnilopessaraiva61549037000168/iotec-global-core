import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
// Painel Principal do Complexo IO // Este ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o esqueleto de um sistema interativo com teclado mutante, painel dinÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢mico, avatar da IO e integraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o com mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltiplos ambientes

import React, { useState, useEffect } from 'react'; import { Button } from '@/components/ui/button'; import { Card, CardContent } from '@/components/ui/card'; import { Mic, Home, RefreshCw, Eye } from 'lucide-react'; import { motion } from 'framer-motion';

const ambientes = [ "Dados JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dicos", "EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Futurista", "Ecossistemas Digitais", "ImportaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o e Portos", "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde & Biotecnologia", "IA para JustiÃƒÆ'Ã†â€™a", "Moda e Arquitetura", ];

const teclados = { padrao: ["Painel", "Projetos", "MissÃƒÆ'Ã†â€™o", "Contato"], dados: ["Big Data", "API Streaming", "Dashboards", "ExtraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"], educativo: ["Aulas", "Metodologias", "IA PedagÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica", "Tutores"], acessibilidade: ["Autismo", "ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âudio descriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", "Libras", "Fontes A+"], };

export default function ComplexoPanel() { const [modo, setModo] = useState("padrao"); const [ambiente, setAmbiente] = useState(0); const [painel, setPainel] = useState(teclados[modo]); const [hovered, setHovered] = useState(false);

useEffect(() => { setPainel(teclados[modo]); }, [modo]);

function avancarAmbiente() { setAmbiente((prev) => (prev + 1) % ambientes.length); }

return (

Complexo IO ÃƒÆ'Ã…Â½Ãƒâ€šÃ‚Â©

Mudar Ambiente <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4"> {painel.map((item, index) => ( <Card key={index} onMouseEnter={() => setHovered(true)} onMouseLeave={() => setHovered(false)} className="cursor-pointer transition hover:scale-105" > <CardContent className="p-6 text-center font-semibold"> {item} </CardContent> </Card> ))} </section> <div className="mt-10 p-6 border-t"> <motion.div className="text-xl text-center" initial={{ opacity: 0 }} animate={{ opacity: 1 }} > Ambiente atual: <strong>{ambientes[ambiente]}</strong> </motion.div> </div> <footer className="mt-6 flex justify-between items-center"> <Button variant="ghost" onClick={() => setModo("padrao")}><Home className="mr-2" />Tela Inicial</Button> <Button variant="outline" onClick={() => setModo("educativo")}><Eye className="mr-2" />Modo Educativo</Button> <Button variant="outline" onClick={() => setModo("acessibilidade")}><Eye className="mr-2" />Acessibilidade</Button> <Button variant="outline" onClick={() => setModo("dados")}><Eye className="mr-2" />Modo Dados</Button> <Button variant="default"><Mic



