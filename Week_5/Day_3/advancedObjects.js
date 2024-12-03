let myObj = {
    name : "John",
    lastName : "Doe",
    age : 25,
    friends : ["Mark", "Lucie", "Ana"]
}

const arrayOfKeys = Object.keys(myObj);
const arrayOfValues = Object.values(myObj);

console.log(`Number of keys is: ${arrayOfKeys.length}\nNumber of values is: ${arrayOfValues.length}`)

let index = 0
for (let [key, value] of Object.entries(myObj)) {
    index++;
    console.log(`The ${index} key is: ${key}. It has a value of ${value}.`);
}