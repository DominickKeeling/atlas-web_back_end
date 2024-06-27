const Utils = {
    calculateNumber(type, a, b) {
        const roundedA = Math.round(a);
        const roundedB = Math.round(b);
        const sum = roundedA + roundedB;
    
        if (type === 'SUM') {
            return roundedA + roundedB;
        } else if (type === 'SUBTRACT') {
            return roundedA - roundedB;
        } else if (type === 'DIVIDE') {
            if (roundedB === 0) {
                return 'Error';
            }
            return roundedA / roundedB;
        } else {
            throw new Error('Invalid operation');
        }
    }
}

module.exports = Utils;
