import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
export default function BlackDiamondPrototype() {
  const sections = [
    {
      title: 'Ecossistema',
      description: 'Entrada principal do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo premium.',
      video:
        'https://videos.pexels.com/video-files/3129957/3129957-uhd_2560_1440_25fps.mp4',
    },
    {
      title: 'Amazon Temple',
      description: 'IgarapÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©s, floresta amazÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´nica e integraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o natureza-tecnologia.',
      video:
        'https://videos.pexels.com/video-files/857195/857195-hd_1920_1080_25fps.mp4',
    },
    {
      title: 'Alpine Wind',
      description: 'Neve, montanhas e silÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncio contemplativo.',
      video:
        'https://videos.pexels.com/video-files/3015510/3015510-uhd_2560_1440_24fps.mp4',
    },
    {
      title: 'Orchid Hall',
      description: 'Luxo silencioso e sofisticaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o visual.',
      video:
        'https://videos.pexels.com/video-files/5532761/5532761-hd_1920_1080_30fps.mp4',
    },
  ];

  return (
    <div className="relative min-h-screen overflow-hidden bg-black text-white">
      <video
        autoPlay
        muted
        loop
        playsInline
        className="absolute inset-0 h-full w-full object-cover opacity-40"
      >
        <source
          src="https://videos.pexels.com/video-files/3129957/3129957-uhd_2560_1440_25fps.mp4"
          type="video/mp4"
        />
      </video>

      <div className="absolute inset-0 bg-gradient-to-b from-black/80 via-black/40 to-black/90" />

      <div className="relative z-10 flex min-h-screen flex-col">
        <header className="flex items-center justify-between border-b border-white/10 px-10 py-6 backdrop-blur-md">
          <div>
            <h1 className="text-3xl font-semibold tracking-[0.4em] text-white">
              BLACK DIAMOND
            </h1>
            <p className="mt-2 text-sm text-zinc-300">
              Tecnologia ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ Natureza ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ CivilizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ ExperiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Premium
            </p>
          </div>

          <nav className="flex gap-4 text-sm text-zinc-300">
            <button className="rounded-2xl border border-white/10 bg-white/5 px-5 py-2 transition hover:bg-white/10">
              Empresa
            </button>
            <button className="rounded-2xl border border-white/10 bg-white/5 px-5 py-2 transition hover:bg-white/10">
              Ecossistema
            </button>
            <button className="rounded-2xl border border-white/10 bg-white/5 px-5 py-2 transition hover:bg-white/10">
              PortfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lio
            </button>
            <button className="rounded-2xl border border-white/10 bg-white/5 px-5 py-2 transition hover:bg-white/10">
              CatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡logo
            </button>
          </nav>
        </header>

        <main className="flex flex-1 flex-col justify-center px-10 py-16">
          <div className="max-w-4xl">
            <h2 className="text-6xl font-light leading-tight text-white">
              Ecossistema Corporativo
              <span className="block text-zinc-400">
                integrado ÃƒÆ'Ã†â€™  natureza e contemplaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.
              </span>
            </h2>

            <p className="mt-8 max-w-2xl text-lg leading-8 text-zinc-300">
              Plataforma premium com ambientes vivos, vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deos automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ticos,
              profundidade visual, integraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o cultural, arquitetura emocional e
              navegaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o cinematogrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡fica.
            </p>

            <div className="mt-10 flex gap-4">
              <button className="rounded-2xl bg-white px-8 py-4 text-sm font-semibold text-black transition hover:scale-105">
                Entrar no Ecossistema
              </button>

              <button className="rounded-2xl border border-white/20 bg-black/30 px-8 py-4 text-sm text-white transition hover:bg-white/10">
                Ver PortfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lio
              </button>
            </div>
          </div>

          <section className="mt-20 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
            {sections.map((item) => (
              <div
                key={item.title}
                className="group relative overflow-hidden rounded-[32px] border border-white/10 bg-white/5 backdrop-blur-xl transition hover:scale-[1.02]"
              >
                <video
                  autoPlay
                  muted
                  loop
                  playsInline
                  className="absolute inset-0 h-full w-full object-cover opacity-30 transition duration-500 group-hover:opacity-50"
                >
                  <source src={item.video} type="video/mp4" />
                </video>

                <div className="relative z-10 flex h-[280px] flex-col justify-end bg-gradient-to-t from-black via-black/30 to-transparent p-6">
                  <div>
                    <h3 className="text-2xl font-semibold text-white">
                      {item.title}
                    </h3>
                    <p className="mt-3 text-sm leading-6 text-zinc-300">
                      {item.description}
                    </p>
                  </div>

                  <button className="mt-6 rounded-2xl border border-white/10 bg-white/10 px-5 py-3 text-sm transition hover:bg-white/20">
                    Explorar Ambiente
                  </button>
                </div>
              </div>
            ))}
          </section>
        </main>

        <footer className="border-t border-white/10 px-10 py-6 text-sm text-zinc-500 backdrop-blur-md">
          NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Premium ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ VÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deos automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ticos obrigatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ Estrutura modular ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢
          Ambientes vivos
        </footer>
      </div>
    </div>
  );
}




