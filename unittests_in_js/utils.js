const Utils = {
    calculateNumber(type, a, b) {
        if (type === 'SUM') {
            return Math.round(a) + Math.round(b);
        } else if (type === 'SUBTRACT') {
            return Math.round(a) - Math.round(b);
        } else if (type === 'DIVIDE') {
        if (Math.round(b) === 0) {
            return 'Error';
        }
        return Math.round(a) / Math.round(b);
        }
    }
};

const Utils = require('./utils');

exports.sendPaymentRequestToApi = function(totalAmount, totalDiscount) {
    const result = Utils.calculateNumber('SUM', totalAmount, totalDiscount);
    console.log(`Sending payment request with result: ${result}`);
};


module.exports = Utils;
