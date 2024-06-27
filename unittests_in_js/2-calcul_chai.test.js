const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
    it('should return 6 when adding 1.4 and 4.5', () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 0 when adding -1.4 and 1.4', () => {
        expect(calculateNumber('SUM', -1.4, 1.4)).to.equal(0);
    });

    it('should return 3 when subtracting 1.4 from 4.4', () => {
        expect(calculateNumber('SUBTRACT', 4.4, 1.4)).to.equal(3);
    });

    it('should return 0.2 when dividing 1.4 by 4.5', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return Error when dividing 1.4 by 0', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});
