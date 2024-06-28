const express = require('express');
const app = express();
const PORT = 7865;

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const { id } = req.params;

  // Validate if :id is a number
  if (isNaN(id)) {
    return res.status(404).send('Invalid cart ID. Must be a number.');
  }

  res.send(`Payment methods for cart ${id}`);
});

module.exports = app;
