// const myArray = [2,3,4,5,6]

// // Using a for each loop to console log each item in the loop

// myArray.forEach((value,index) => {
//     console.log(`Index: ${index}, Value: ${value}`)
// })

// // Console logging each item in the array powered by 2

// myArray.forEach((value,index) => {
//     console.log(`Index: ${index}, Value: ${value**2}`)
// })

// // Updating the array values

// myArray.forEach((value,index) => {
//     myArray[index] = (`Index: ${index}, Value: ${value**2}`)
// })

// console.log(myArray)

// // Exercise 1 

// const numbers = [10,11,12,15,20];

// numbers.forEach((value) => {
//     if (value % 2 === 0) {
//         console.log (value)
//     }
// })

// // Exercise 2

// const words = ["wow","hey","bye"];

// words.some(value => {
//     if(value.startsWith('h')){
//         console.log(true)
//     } else {
//         console.log(false)
//     }
// })

// // Exercise 3
const words = ["hello","hey","hola"];

words.every(value => {
    value.startsWith('h')
})