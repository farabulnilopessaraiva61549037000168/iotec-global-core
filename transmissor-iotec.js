// ==============================================================================
// TRANSMISSOR UNIVERSAL IOTEC BL -> RENDER (IOTEC_PLATFORM-1) / E-MAIL
// ==============================================================================
(function() {
  const RENDER_ENDPOINT = "https://iotec-platform-1.onrender.com/api/pedidos";
  const EMAIL_FALLBACK = "iotec.bl@proton.me";

  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('form').forEach(form => {
      form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        data.origem_portal = window.location.hostname;
        data.data_envio = new Date().toISOString();

        const btn = form.querySelector('button[type="submit"]') || form.querySelector('button') || form.querySelector('a');
        if(btn) btn.innerText = "Transmitindo ao Núcleo...";

        try {
          const response = await fetch(RENDER_ENDPOINT, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          });

          if (response.ok) {
            alert("✅ Pedido transmitido com sucesso ao Núcleo IOTEC BL!");
            form.reset();
          } else {
            throw new Error("Falha no envio");
          }
        } catch (err) {
          window.location.href = mailto:?subject=Novo Pedido via &body= + encodeURIComponent(JSON.stringify(data, null, 2));
        }
      });
    });
  });
})();