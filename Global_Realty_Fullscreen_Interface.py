import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
export default function IOTECGlobalRealty() {

  const properties = [

    {

      title: 'Luxury Residence Miami',

      location: 'Miami, Florida',

      price: '$2.8M',

      image: 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?q=80&w=1600&auto=format&fit=crop'

    },

    {

      title: 'Downtown Commercial Tower',

      location: 'Orlando, Florida',

      price: '$4.2M',

      image: 'https://images.unsplash.com/photo-1494526585095-c41746248156?q=80&w=1600&auto=format&fit=crop'

    },

    {

      title: 'Ocean View Penthouse',

      location: 'Los Angeles, California',

      price: '$6.1M',

      image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=1600&auto=format&fit=crop'

    }

  ];



  return (

    <div className="min-h-screen bg-black text-white overflow-hidden">

      <div className="relative h-screen w-full">

        <img

          src="https://images.unsplash.com/photo-1460317442991-0ec209397118?q=80&w=2000&auto=format&fit=crop"

          alt="Luxury Skyline"

          className="absolute inset-0 w-full h-full object-cover opacity-40"

        />



        <div className="absolute inset-0 bg-gradient-to-b from-black/70 via-black/40 to-black" />



        <header className="relative z-10 flex items-center justify-between px-10 py-6 border-b border-white/10 backdrop-blur-sm">

          <div>

            <h1 className="text-3xl font-bold tracking-[0.25em]">IOTEC GLOBAL REALTY</h1>

            <p className="text-sm text-zinc-300 mt-1">Intelligent Property Operations</p>

          </div>



          <nav className="hidden md:flex gap-8 text-sm text-zinc-200">

            <span className="hover:text-white cursor-pointer">Luxury</span>

            <span className="hover:text-white cursor-pointer">Commercial</span>

            <span className="hover:text-white cursor-pointer">Rentals</span>

            <span className="hover:text-white cursor-pointer">Investments</span>

            <span className="hover:text-white cursor-pointer">Analytics</span>

          </nav>

        </header>



        <div className="relative z-10 h-[calc(100vh-100px)] flex flex-col justify-center px-10 lg:px-20">

          <div className="max-w-4xl">

            <p className="uppercase tracking-[0.4em] text-zinc-300 text-sm mb-6">

              Global Intelligent Realty Platform

            </p>



            <h2 className="text-5xl lg:text-8xl font-black leading-tight mb-8">

              The Future Of

              <span className="block text-zinc-300">Luxury Realty</span>

            </h2>



            <p className="text-lg text-zinc-300 max-w-2xl leading-relaxed mb-10">

              High-end real estate operations, investment intelligence,

              lead orchestration and global property visualization in a

              single executive platform.

            </p>



            <div className="flex flex-wrap gap-4">

              <button className="px-8 py-4 rounded-2xl bg-white text-black font-semibold hover:scale-105 transition-all shadow-2xl">

                Explore Properties

              </button>



              <button className="px-8 py-4 rounded-2xl border border-white/30 bg-white/10 backdrop-blur-md hover:bg-white/20 transition-all">

                Contact IOTEC

              </button>

            </div>

          </div>

        </div>

      </div>



      <section className="px-8 lg:px-16 py-20 bg-zinc-950">

        <div className="flex items-center justify-between mb-12">

          <div>

            <h3 className="text-4xl font-bold mb-3">Premium Properties</h3>

            <p className="text-zinc-400 max-w-xl">

              Curated luxury assets monitored by the IOTEC operational core.

            </p>

          </div>



          <div className="hidden lg:flex gap-6 text-right">

            <div>

              <p className="text-3xl font-bold">248</p>

              <p className="text-zinc-400 text-sm">Active Listings</p>

            </div>



            <div>

              <p className="text-3xl font-bold">US$ 84M</p>

              <p className="text-zinc-400 text-sm">Portfolio Value</p>

            </div>

          </div>

        </div>



        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

          {properties.map((property, index) => (

            <div

              key={index}

              className="group bg-zinc-900 rounded-[2rem] overflow-hidden border border-white/5 hover:border-white/20 transition-all hover:-translate-y-2 shadow-2xl"

            >

              <div className="relative h-80 overflow-hidden">

                <img

                  src={property.image}

                  alt={property.title}

                  className="w-full h-full object-cover group-hover:scale-110 transition-all duration-700"

                />



                <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent" />



                <div className="absolute bottom-6 left-6">

                  <p className="text-3xl font-bold">{property.price}</p>

                </div>

              </div>



              <div className="p-8">

                <h4 className="text-2xl font-bold mb-2">{property.title}</h4>

                <p className="text-zinc-400 mb-6">{property.location}</p>



                <div className="flex items-center justify-between">

                  <div className="flex gap-4 text-sm text-zinc-400">

                    <span>Luxury</span>

                    <span>Premium</span>

                    <span>Smart Analytics</span>

                  </div>



                  <button className="px-5 py-3 rounded-xl bg-white text-black font-medium hover:scale-105 transition-all">

                    View

                  </button>

                </div>

              </div>

            </div>

          ))}

        </div>

      </section>



      <section className="px-8 lg:px-16 py-20 bg-black border-t border-white/5">

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">

          <div>

            <p className="uppercase tracking-[0.35em] text-zinc-400 text-sm mb-4">

              Executive Control Tower

            </p>



            <h3 className="text-5xl font-black mb-8 leading-tight">

              Full Operational

              <span className="block text-zinc-400">Visibility</span>

            </h3>



            <div className="space-y-5 text-zinc-300 text-lg leading-relaxed">

              <p>

                Global monitoring of properties, leads, commissions,

                negotiations and strategic market opportunities.

              </p>



              <p>

                Integrated with the IOTEC operational gateway for premium

                client acquisition and intelligent real estate analytics.

              </p>

            </div>

          </div>



          <div className="bg-zinc-950 rounded-[2rem] border border-white/10 p-10 shadow-2xl">

            <div className="grid grid-cols-2 gap-6">

              <div className="bg-white/5 rounded-2xl p-6 border border-white/5">

                <p className="text-zinc-400 text-sm mb-2">New Leads</p>

                <h4 className="text-4xl font-bold">128</h4>

              </div>



              <div className="bg-white/5 rounded-2xl p-6 border border-white/5">

                <p className="text-zinc-400 text-sm mb-2">Closed Deals</p>

                <h4 className="text-4xl font-bold">42</h4>

              </div>



              <div className="bg-white/5 rounded-2xl p-6 border border-white/5">

                <p className="text-zinc-400 text-sm mb-2">Monthly Revenue</p>

                <h4 className="text-3xl font-bold">US$ 380K</h4>

              </div>



              <div className="bg-white/5 rounded-2xl p-6 border border-white/5">

                <p className="text-zinc-400 text-sm mb-2">Active Markets</p>

                <h4 className="text-4xl font-bold">12</h4>

              </div>

            </div>



            <div className="mt-10 bg-gradient-to-r from-white/10 to-white/5 rounded-2xl p-6 border border-white/10">

              <p className="text-zinc-400 mb-2">Gateway Contact</p>

              <h4 className="text-2xl font-bold">iotec.bl@proton.me</h4>

              <p className="text-zinc-500 mt-3 text-sm">

                Premium client acquisition and intelligent operational gateway.

              </p>

            </div>

          </div>

        </div>

      </section>

    </div>

  );

}







