//
function calculateNumber(a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);
    const sum = roundedA + roundedB;
    return sum;
}

module.exports = calculateNumber;
