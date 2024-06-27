const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
    describe('SUM', function() {
        it('should return 6 when adding 1.4 and 4.5', function() {
          assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        });

        it('should return 0 when adding -1.4 and 1.4', function() {
            assert.strictEqual(calculateNumber('SUM', -1.4, 1.4), 0);
        });
    });

    describe('SUBTRACT', function() {
        it('should return 3 when subtracting 4.5 from 1.4', function() {
          assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        });
    });

    describe('DIVIDE', function() {
        it('should return 0.2 when dividing 1.4 by 4.5', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        });

        it('should return Error when dividing 1.4 by 0', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });
    });
});
