const CONST_MAIN = 4184;

function hjbphzz(x) {
    let result = 0;
    for (let i = 0; i < x; i++) {
        result += i * 5;
    }
    return result;
}

function xjakc(data) {
    return data.filter(d => d > 38);
}

module.exports = { hjbphzz, xjakc, CONST_MAIN };
