import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
// Painel de CaptaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o MultinÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel - SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Visual com React + Tailwind + Framer Motion // Comportamento de entradas de dados por camadas e projeÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes financeiras

import { useState, useEffect } from 'react'; import { Card, CardContent } from "@/components/ui/card"; import { motion } from "framer-motion"; import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const layers = ["Atmosfera Digital", "SuperfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cie", "Subsolo", "Dados Submersos"];

const generateSimulatedData = () => { return layers.map((layer, index) => ({ layer, value: Math.floor(Math.random() * (10000 - 1000) + 1000), })); };

const calculateProjection = (layerData) => { return layerData.reduce((acc, curr, idx) => { const tax = 0.25; // imposto 25% const net = curr.value * (1 - tax); acc.push({ name: curr.layer, Bruto: curr.value, LÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­quido: parseFloat(net.toFixed(2)) }); return acc; }, []); };

export default function PainelCaptacao() { const [layerData, setLayerData] = useState(generateSimulatedData()); const [projection, setProjection] = useState([]);

useEffect(() => { setProjection(calculateProjection(layerData)); }, [layerData]);

return (

Painel de CaptaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o MultinÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel

<div className="grid grid-cols-1 md:grid-cols-2 gap-6"> {layerData.map((layer, idx) => ( <motion.div key={idx} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: idx * 0.2 }}> <Card> <CardContent> <h2 className="text-xl font-semibold">{layer.layer}</h2> <p className="text-green-600 text-2xl font-bold">R$ {layer.value.toLocaleString()}</p> </CardContent> </Card> </motion.div> ))} </div> <div className="mt-12"> <h2 className="text-2xl font-bold mb-4">ProjeÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de Receita (Bruto x LÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­quido)</h2> <ResponsiveContainer width="100%" height={300}> <




