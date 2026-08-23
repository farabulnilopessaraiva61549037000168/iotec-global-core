import useSWR from 'swr';
const fetcher = url => fetch(url).then(r => r.json());

export default function Gallery() {
  const { data } = useSWR(
    process.env.NEXT_PUBLIC_REGULUS_API_URL + '/media/recent',
    fetcher
  );

  if (!data) return <div>Carregando mídia...</div>;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3,1fr)', gap: 12 }}>
      {data.items.map((m) => (
        <div key={m.id} style={{ border: '1px solid #eee', padding: 8 }}>
          <img src={m.thumb} alt={m.title} style={{ width: '100%' }} />
          <div>{m.title}</div>
        </div>
      ))}
    </div>
  );
}

