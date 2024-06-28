const request = require('request');
const expect = require('chai').expect;

describe('Index page', () => {
    const baseUrl = 'http://localhost:7865';

    it('should return the correct status code', (done) => {
        request.get(baseUrl, (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return the correct result', (done) => {
        request.get(baseUrl, (error, response, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});
