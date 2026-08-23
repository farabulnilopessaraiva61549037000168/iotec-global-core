import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
mport React from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function PainelComplexo() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-50 to-white p-6">
      <header className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Bem-vindo ao Complexo IO</h1>
        <p className="text-lg text-gray-500 mt-2">
          Uma holding digital para o futuro da humanidade.
        </p>
      </header>

      <section className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* CARD 1: O que ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o Complexo */}
        <Card className="shadow-xl">
          <CardContent>
            <h2 className="text-xl font-semibold text-blue-800 mb-2">O que ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o Complexo?</h2>
            <p className="text-gray-600">
              O Complexo IO ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© um ecossistema digital inspirado em inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia artificial, natureza e engenharia simbÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lica.
              Funciona como uma cidade inteligente e interativa, oferecendo soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes, produtos e serviÃƒÆ'Ã†â€™os 24h.
            </p>
          </CardContent>
        </Card>

        {/* CARD 2: Como ele funciona */}
        <Card className="shadow-xl">
          <CardContent>
            <h2 className="text-xl font-semibold text-green-800 mb-2">Como funciona?</h2>
            <p className="text-gray-600">
              CaptaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de dados, mineraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de trÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡fego digital, integraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o com fontes pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblicas e privadas.
              Tudo isso gera receita, com controle fiscal, margem lÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­quida segura e reinvestimento em inovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.
            </p>
          </CardContent>
        </Card>

        {/* CARD 3: O que posso fazer aqui? */}
        <Card className="shadow-xl">
          <CardContent>
            <h2 className="text-xl font-semibold text-purple-800 mb-2">O que posso fazer?</h2>
            <p className="text-gray-600">
              Acesse serviÃƒÆ'Ã†â€™os, compre produtos, aprenda sobre tecnologia, integre-se como criador ou investidor.
              Tudo com base em ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica, dados e inovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.
            </p>
          </CardContent>
        </Card>

        {/* CARD 4: VisÃƒÆ'Ã†â€™o e MissÃƒÆ'Ã†â€™o */}
        <Card className="shadow-xl">
          <CardContent>
            <h2 className="text-xl font-semibold text-yellow-800 mb-2">MissÃƒÆ'Ã†â€™o & VisÃƒÆ'Ã†â€™o</h2>
            <p className="text-gray-600">
              Ser a ponte entre o digital e o humano. Oferecer uma plataforma sustentÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel, com inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia orgÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢nica,
              acessÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel, inclusiva e de alto impacto social e tecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gico.
            </p>
          </CardContent>
        </Card>
      </section>

      {/* BotÃƒÆ'Ã†â€™o interativo */}
      <div className="text-center mt-10">
        <Button className="bg-black text-white px-6 py-2 text-lg rounded-full shadow-lg hover:bg-gray-900">
          Explorar o Complexo
        </Button>
      </div>
    </div>
  );
}



