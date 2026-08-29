const Service = require('node-windows').Service;

// Cria o objeto do serviço Windows
const svc = new Service({
  name: 'IOTEC_WPPConnect',
  description: 'Servico local de disparos de mensagens e boletos da IOTEC via WPPConnect',
  script: 'C:\\IOTEC\\wppconnect-server\\index.js',
  nodeOptions: []
});

// Evento disparado quando o serviço termina de instalar
svc.on('install', function() {
  console.log('[✔] Servico IOTEC_WPPConnect instalado com sucesso!');
  svc.start();
});

// Instala o serviço
svc.install();