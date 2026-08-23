export default function DipPanel({ status }) {
  return (
    <div style={{ border: '1px solid #ddd', padding: 12, borderRadius: 8 }}>
      <h3>DIP° — Painel</h3>
      <p>Núcleo Principal: {status?.nucleo ?? '—'}</p>
      <p>Nuvem: {status?.nuvem ?? '—'}</p>
      <p>Módulos: {status?.modulos ? status.modulos.join(', ') : '—'}</p>
    </div>
  );
}

