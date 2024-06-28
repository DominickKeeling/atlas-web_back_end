const chai = require('chai');
const sinon = require('sinon');
const expect = chai.expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
    it('should call Utils.calculateNumber with SUM, 100, 20', () => {
        const spy = sinon.spy(Utils, 'calculateNumber');

        sendPaymentRequestToApi(100, 20);

        expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

        spy.restore();
        console.log(`restored`);
    });
});
