const request = require('request');
const expect = require('chai').expect;
const chaiHttp = require('chai-http');

chai.use(chaiHttp);

describe('Cart Page', () => {
    it('should return status 200 and payment methods for valid cart ID', (done) => {
        chai.request(app)
            .get('/cart/12')
            .end((err, res) => {
                expect(res).to.have.status(200);
                expect(res.text).to.equal('Payment methods for cart 12');
                done(); 
            });
    });

    it('should return status 404 for non-numeric cart ID', (done) => {
        chai.request(app)
            .get('/cart/hello')
            .end((err, res) => {
                expect(res).to.have.status(404);
                expect(res.text).to.equal('Invalid cart ID. Must be a number.');
                done();
            });
    });
});
