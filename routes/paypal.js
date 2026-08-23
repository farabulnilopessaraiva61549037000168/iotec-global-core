const express = require('express');
const paypal = require('@paypal/checkout-server-sdk');

const router = express.Router();

// Configuração do ambiente PayPal
const environment = new paypal.core.LiveEnvironment(
  process.env.PAYPAL_CLIENT_ID,
  process.env.PAYPAL_CLIENT_SECRET
);
const client = new paypal.core.PayPalHttpClient(environment);

// Rota para criar ordem de pagamento
router.post('/criar-ordem', async (req, res) => {
  const request = new paypal.orders.OrdersCreateRequest();
  request.prefer("return=representation");
  request.requestBody({
    intent: 'CAPTURE',
    purchase_units: [{
      amount: {
        currency_code: 'BRL',
        value: (req.body.preco || 10.0).toString()
      }
    }]
  });

  try {
    const order = await client.execute(request);
    res.json({ id: order.result.id, status: order.result.status, links: order.result.links });
  } catch (error) {
    console.error('Erro no PayPal:', error);
    res.status(500).json({ error: 'Erro ao gerar ordem no PayPal' });
  }
});

module.exports = router;
