import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
export default function IOTECControlCenter() {

  const systems = [

    { name: 'NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO', status: 'ONLINE', port: 5000 },

    { name: 'WATCHER', status: 'ONLINE', port: 5001 },

    { name: 'WEB OBSERVER', status: 'ONLINE', port: 5020 },

    { name: 'TRAFFIC CONTROL', status: 'ONLINE', port: 5050 },

  ];



  const alerts = [

    'PoluiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o visual detectada em interface Netlify',

    'ServiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Render nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o configurado',

    'Assets incompletos detectados',

  ];



  return (

    <div className="w-screen h-screen overflow-hidden bg-black text-white relative">

      {/* Background */}

      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(0,180,255,0.12),transparent_60%)]" />

      <div className="absolute inset-0 opacity-20">

        <div className="w-full h-full bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:40px_40px]" />

      </div>



      {/* Header */}

      <div className="relative z-10 h-20 border-b border-cyan-500/30 backdrop-blur-xl flex items-center justify-between px-8 bg-black/40">

        <div>

          <h1 className="text-3xl font-bold tracking-widest text-cyan-400">

            IOTEC CENTRAL OPERACIONAL

          </h1>

          <p className="text-sm text-cyan-200/70 mt-1">

            Infraestrutura Modular ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ SupervisÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Perimetral ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Monitoramento Inteligente

          </p>

        </div>



        <div className="flex gap-6 items-center">

          <div className="text-right">

            <div className="text-xs text-gray-400">STATUS GLOBAL</div>

            <div className="text-green-400 font-bold tracking-wider">

              OPERACIONAL

            </div>

          </div>



          <div className="w-4 h-4 rounded-full bg-green-400 animate-pulse shadow-[0_0_20px_#00ff88]" />

        </div>

      </div>



      {/* Main Grid */}

      <div className="relative z-10 grid grid-cols-12 grid-rows-12 gap-4 p-4 h-[calc(100vh-80px)]">



        {/* Left Perimeter */}

        <div className="col-span-2 row-span-12 rounded-3xl border border-cyan-500/20 bg-black/40 backdrop-blur-xl p-4 flex flex-col gap-4 shadow-2xl">

          <h2 className="text-cyan-400 text-lg font-bold tracking-wider border-b border-cyan-500/20 pb-2">

            SERVIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡OS

          </h2>



          {systems.map((system, index) => (

            <div

              key={index}

              className="rounded-2xl border border-cyan-500/10 bg-cyan-500/5 p-4 hover:bg-cyan-500/10 transition-all"

            >

              <div className="flex items-center justify-between mb-2">

                <span className="font-semibold text-sm tracking-wide">

                  {system.name}

                </span>



                <div className="w-3 h-3 rounded-full bg-green-400 shadow-[0_0_10px_#00ff88] animate-pulse" />

              </div>



              <div className="text-xs text-gray-400">

                PORTA: {system.port}

              </div>



              <div className="text-green-400 text-xs mt-2 font-bold tracking-wider">

                {system.status}

              </div>

            </div>

          ))}

        </div>



        {/* Center Tactical Panel */}

        <div className="col-span-8 row-span-12 rounded-3xl border border-cyan-500/20 bg-black/30 backdrop-blur-xl overflow-hidden shadow-[0_0_80px_rgba(0,255,255,0.08)] relative">



          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(0,255,255,0.08),transparent_70%)]" />



          <div className="relative z-10 p-6 h-full flex flex-col">



            <div className="flex items-center justify-between mb-6">

              <div>

                <h2 className="text-2xl font-bold text-cyan-300 tracking-widest">

                  MAPA OPERACIONAL

                </h2>

                <p className="text-gray-400 text-sm mt-1">

                  SupervisÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o em tempo real da malha operacional IOTEC

                </p>

              </div>



              <div className="flex gap-3">

                <div className="px-4 py-2 rounded-xl bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 text-sm">

                  WATCHER ATIVO

                </div>



                <div className="px-4 py-2 rounded-xl bg-green-500/10 border border-green-500/20 text-green-300 text-sm">

                  TRÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂFEGO ESTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEL

                </div>

              </div>

            </div>



            {/* Radar Center */}

            <div className="flex-1 rounded-3xl border border-cyan-500/10 relative overflow-hidden bg-black/50">



              <div className="absolute inset-0 flex items-center justify-center">

                <div className="w-[650px] h-[650px] rounded-full border border-cyan-500/20 animate-pulse relative">



                  <div className="absolute inset-10 rounded-full border border-cyan-400/10" />

                  <div className="absolute inset-20 rounded-full border border-cyan-400/10" />

                  <div className="absolute inset-32 rounded-full border border-cyan-400/10" />



                  <div className="absolute left-1/2 top-0 bottom-0 w-px bg-cyan-500/20" />

                  <div className="absolute top-1/2 left-0 right-0 h-px bg-cyan-500/20" />



                  <div className="absolute inset-0 animate-spin [animation-duration:12s] origin-center">

                    <div className="absolute left-1/2 top-1/2 w-[320px] h-[2px] bg-gradient-to-r from-cyan-400 to-transparent origin-left shadow-[0_0_20px_#00ffff]" />

                  </div>



                  <div className="absolute left-[45%] top-[30%] w-4 h-4 rounded-full bg-green-400 shadow-[0_0_15px_#00ff88] animate-ping" />

                  <div className="absolute left-[65%] top-[55%] w-4 h-4 rounded-full bg-cyan-400 shadow-[0_0_15px_#00ffff] animate-ping" />

                  <div className="absolute left-[30%] top-[60%] w-4 h-4 rounded-full bg-blue-400 shadow-[0_0_15px_#00bbff] animate-ping" />

                </div>

              </div>



              <div className="absolute bottom-6 left-6 right-6 grid grid-cols-4 gap-4">

                <div className="rounded-2xl bg-black/60 border border-cyan-500/10 p-4">

                  <div className="text-gray-400 text-xs">INTERFACES</div>

                  <div className="text-3xl font-bold text-cyan-300 mt-2">12</div>

                </div>



                <div className="rounded-2xl bg-black/60 border border-cyan-500/10 p-4">

                  <div className="text-gray-400 text-xs">PORTAS ATIVAS</div>

                  <div className="text-3xl font-bold text-green-300 mt-2">4</div>

                </div>



                <div className="rounded-2xl bg-black/60 border border-cyan-500/10 p-4">

                  <div className="text-gray-400 text-xs">WATCHERS</div>

                  <div className="text-3xl font-bold text-blue-300 mt-2">3</div>

                </div>



                <div className="rounded-2xl bg-black/60 border border-cyan-500/10 p-4">

                  <div className="text-gray-400 text-xs">ESTABILIDADE</div>

                  <div className="text-3xl font-bold text-purple-300 mt-2">98%</div>

                </div>

              </div>

            </div>

          </div>

        </div>



        {/* Right Perimeter */}

        <div className="col-span-2 row-span-12 rounded-3xl border border-red-500/20 bg-black/40 backdrop-blur-xl p-4 flex flex-col shadow-2xl">

          <h2 className="text-red-400 text-lg font-bold tracking-wider border-b border-red-500/20 pb-2">

            ALERTAS

          </h2>



          <div className="flex-1 overflow-auto mt-4 space-y-4">

            {alerts.map((alert, index) => (

              <div

                key={index}

                className="rounded-2xl border border-red-500/20 bg-red-500/5 p-4"

              >

                <div className="flex items-start gap-3">

                  <div className="w-3 h-3 rounded-full bg-red-400 mt-1 shadow-[0_0_12px_#ff4444] animate-pulse" />



                  <div>

                    <div className="text-sm font-semibold text-red-300">

                      ALERTA OPERACIONAL

                    </div>



                    <div className="text-xs text-red-200/70 mt-2 leading-relaxed">

                      {alert}

                    </div>

                  </div>

                </div>

              </div>

            ))}

          </div>



          <div className="mt-4 rounded-2xl border border-cyan-500/10 bg-cyan-500/5 p-4">

            <div className="text-xs text-gray-400 mb-2">

              OBSERVAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O SISTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ MICA

            </div>



            <div className="text-sm text-cyan-200 leading-relaxed">

              Infraestrutura supervisionada continuamente por entidades watcher e observer.

            </div>

          </div>

        </div>

      </div>

    </div>

  );

}







