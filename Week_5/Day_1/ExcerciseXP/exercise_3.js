// 1 - Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
// Check out the example below to see the expected output

// console.log(isString('hello')); 
// //true
// console.log(isString([1, 2, 4, 0]));
// //false

const isThisAString = input => typeof input === "string" ? true : false

console.log(isThisAString("hellooooo"))
console.log(isThisAString(21321))
console.log(isThisAString([1,"2"]))