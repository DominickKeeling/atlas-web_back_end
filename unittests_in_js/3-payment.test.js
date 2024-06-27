const chai = require('chai');
const sinon = require('sinon');
const expect = chai.expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
    let calculateNumberSpy;

    beforeEach(() => {
        calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    });

    afterEach(() => {
        calculateNumberSpy.restore();
    });

    it('should call Utils.calculateNumber with SUM, 100, 20', () => {
        const consoleSpy = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20);
        expect(calculateNumberSpy.calledOnceWith('SUM', 100, 20)).to.be.true;
        expect(consoleSpy.calledOnceWith('The total is: 120')).to.be.true;
        consoleSpy.restore();
    });
});
