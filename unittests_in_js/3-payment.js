const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const result = Utils.calculatNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is : ${result}`);
}

module.experts = sendPaymentRequestToApi;
