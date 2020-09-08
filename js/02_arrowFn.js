function product(a, b){
    return a * b;
};
console.log(`Product is: ${product(1, 10)}`);

multiple = () => 2 * 10;
multiple1 = a => a * 10;
multiple2 = (a,b) => a * b;

console.log(`Multiple => is: ${multiple()}`);
console.log(`Multiple1 => is: ${multiple1(3)}`);
console.log(`Multiple2 => is: ${multiple2(4, 10)}`);
