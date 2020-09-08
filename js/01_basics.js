let name = "Steve";
name = "John"
console.log(`Name is: ${name}`);

const newName = "John"
console.log(`New Const name is: ${newName}`);

let age = 19;
console.log(`Age is: ${age}`)


// Conditional Operators
let ageMoreThan18 = false;
if (age > 18){
    ageMoreThan18 = true;
}
else if (age === 18){
    ageMoreThan18 = false;
};
console.log(`Age is more than 18: ${ageMoreThan18}`);

let ageLessThan18 = (age < 18) ? true : false;
console.log(`Age is less than 18: ${ageLessThan18}`);

// Loops
let i =0;
while (i < 5){
  console.log(`i is now ${i}`);
  i++;
};

for (let j=5; j<11; j++){
  console.log(`j is now ${j}`);
};


// Functions
function product(a, b){
    return a * b;
};
console.log(`Product of 16 and 15 is ${product(16, 15)}`);
