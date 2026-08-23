const express = require('express');
const { MercadoPagoConfig, Preference } = require('mercadopago');

const router = express.Router();

const client = new MercadoPagoConfig({
  accessToken: process.env.MERCADOPAGO_ACCESS_TOKEN
});

// Rota para criar preferência de pagamento
router.post('/criar-preferencia', async (req, res) => {
  try {
    const preference = new Preference(client);
    const result = await preference.create({
      body: {
        items: [
          {
            title: req.body.titulo || 'Produto/Serviço IOTEC',
            unit_price: Number(req.body.preco) || 10.0,
            quantity: 1,
            currency_id: 'BRL'
          }
        ]
      }
    });

    res.json({ id: result.id, init_point: result.init_point });
  } catch (error) {
    console.error('Erro no Mercado Pago:', error);
    res.status(500).json({ error: 'Erro ao gerar pagamento com Mercado Pago' });
  }
});

module.exports = router;
