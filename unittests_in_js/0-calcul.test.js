const assert = require('assert')
const calculateNumber = require('./0-calcul')

describe('calculateNumber', () => {
    it('should return 4 when adding 1 and 3', () => {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return the sum of 3.7 and 1, with the first number rounded up', () => {
        assert.strictEqual(calculateNumber(3.7, 1), 5);
    });

    it('should return 5 when adding 1.2 and 3.7', () => {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should return 3 when adding 1.5 and 3.7', () => {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should return 6 when adding 2.2 and 3.7', () => {
        assert.strictEqual(calculateNumber(2.2, 3.7), 6);
    });
});
