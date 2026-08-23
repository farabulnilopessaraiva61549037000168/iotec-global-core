import useSWR from 'swr';
import DipPanel from '../components/DipPanel';
import Gallery from '../components/Gallery';

const fetcher = url => fetch(url).then(r => r.json());

export default function Home() {
  const { data: status } = useSWR(
    process.env.NEXT_PUBLIC_REGULUS_API_URL + '/status',
    fetcher,
    { refreshInterval: 5000 }
  );

  return (
    <main style={{ padding: 24, fontFamily: 'Inter, sans-serif' }}>
      <h1>VERSIO — REGULUS Visual Portal</h1>
      <section style={{ marginTop: 16 }}>
        <h2>STATUS RÁPIDO</h2>
        <pre>{status ? JSON.stringify(status, null, 2) : 'Carregando status...'}</pre>
      </section>

      <section style={{ marginTop: 24 }}>
        <DipPanel status={status} />
      </section>

      <section style={{ marginTop: 24 }}>
        <h2>Galeria / Mídia</h2>
        <Gallery />
      </section>
    </main>
  );
}

