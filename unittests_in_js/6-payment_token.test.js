const chai = require('chai');
const expect = chai.expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('should resolve with {"Success response from the API"} when true'), () => {
        return getPaymentTokenFromAPI(true)
            .then((response) => {
                expect(response).to.deep.equal({ data: 'Successful response from the API' });
                done();
            });
    };

    it('should reject with {"Error response from the API"} when false'), () => {
        return getPaymentTokenFromAPI(false)
            .then((response) => {
                done(new Error('Expected promise to be rejected, but it was resolved'));
            })
            .catch((error) => {
                expect(error.message).to.equal('API request failed');
                done(error);
            });
    };
});
