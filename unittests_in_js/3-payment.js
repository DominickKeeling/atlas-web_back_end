const Utils = require('./utils');

exports.sendPaymentRequestToApi = function(totalAmount, totalDiscount) {
    const result = Utils.calculateNumber('SUM', totalAmount, totalDiscount);
    console.log(`Sending payment request with result: ${result}`);
};

module.exports = sendPaymentRequestToApi;
