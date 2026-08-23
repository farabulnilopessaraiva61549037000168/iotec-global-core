import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button";
import { useState } from "react";
const aldeias = [ { nome: "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde", descricao: "AvanÃƒÆ'Ã†â€™os mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dicos, cura e bem-estar", cor: "bg-green-200" }, { nome: "Moda", descricao: "Estilo, passarelas e inovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica", cor: "bg-pink-200" }, { nome: "EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", descricao: "Tecnologia na aprendizagem e culturas", cor: "bg-blue-200" }, { nome: "Futuro", descricao: "Cidades tecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gicas, SpaceX, Tesla", cor: "bg-purple-200" }, { nome: "Terra", descricao: "Montanhas, florestas, agricultura", cor: "bg-yellow-200" }, { nome: "Arte", descricao: "Esculturas, design e experiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias visuais", cor: "bg-red-200" } ];

export default function PainelComplexo() { const [selecionado, setSelecionado] = useState(null);

return (

ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Hall de Entrada do Complexo

Escolha um dos guichÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs para entrar numa Aldeia do Conhecimento

<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"> {aldeias.map((aldeia, index) => ( <Card key={index} className={`${aldeia.cor} shadow-xl cursor-pointer`} onClick={() => setSelecionado






