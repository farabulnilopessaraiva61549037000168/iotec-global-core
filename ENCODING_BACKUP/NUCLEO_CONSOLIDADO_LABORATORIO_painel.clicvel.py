import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
// ProtÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³tipo inicial de painel clicÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel replicÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel do Complexo Global import { useState } from "react"; import { Card, CardContent } from "@/components/ui/card"; import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog"; import { Button } from "@/components/ui/button";

const aldeias = [ { id: 1, nome: "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde", cor: "bg-green-100", descricao: "AvanÃƒÆ'Ã†â€™os, terapias e curas." }, { id: 2, nome: "Moda", cor: "bg-blue-100", descricao: "EstÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica, MilÃƒÆ'Ã†â€™o, Paris, vestuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio." }, { id: 3, nome: "EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", cor: "bg-yellow-100", descricao: "Saberes, escolas e cultura global." }, { id: 4, nome: "Futuro", cor: "bg-purple-100", descricao: "Tecnologias, carros voadores, SpaceX." }, { id: 5, nome: "Terra", cor: "bg-emerald-100", descricao: "Montanhas, campo, floresta, agricultura." }, { id: 6, nome: "Arte", cor: "bg-pink-100", descricao: "CivilizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes, design, escultura, Petra." }, ];

export default function PainelComplexo() { const [aldeiaSelecionada, setAldeiaSelecionada] = useState(null);

return (

{aldeias.map((aldeia) => ( <Card key={aldeia.id} className={${aldeia.cor} p-4 hover:scale-105 transition-transform cursor-pointer shadow-xl rounded-2xl} onClick={() => setAldeiaSelecionada(aldeia)} >

{aldeia.nome}

{aldeia.descricao}

))}






