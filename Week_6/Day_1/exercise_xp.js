// EXERCISE 1

// function compareToTen(num) {
//     return new Promise((resolve, reject) => {
//         if (num <= 10) {
//             resolve('Number is less or equal to ten.')
//         } else{
//             reject('Number is more then 10.')
//         }
    
// })}

// EXERCISE 2

// function delayedResolvePromise(){
//     return new Promise((resolve, reject) => {
//         setInterval(() => {
//             resolve('Successfully resolved after four seconds.')
//         }, 4000)
//     })
// }

// delayedResolvePromise().then((message) => console.log(message));

// EXERCISE 3

const myPromise = Promise.resolve(3);
myPromise.then(value => console.log(value))

const mySecondPromise = Promise.reject("Boo!")
mySecondPromise.catch(value => console.log(value))