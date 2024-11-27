// // Exercise 1
// function displayNumbersDivisible(divisor) {
//     let totalDivisibleNumbers = 0

//     for (var i = 0; i <= 500; i++){
//         if (i % divisor == 0){
//             console.log(i);
//             totalDivisibleNumbers += i;
//         }
//     }
//     console.log(totalDivisibleNumbers)
// }
// displayNumbersDivisible(23)

// // Exercise 2
// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// const shoppingList = ["banana","orange","apple","cheesecake"]

// function myBill() {
//     // Loop through each item in shopping list
//     for (let item of shoppingList){

//         // Check if the item exists
//         if (item in stock) {
//             // If item exists, check if stock greater then 0
//             if (stock[item] > 0) {
//                 console.log(`${item} is in stock`)
//                 console.log(`${item} costs $${prices[item]}`)
//                 stock[item] -= 1
//             } else {
//                 console.log(`${item} is out of stock.`)
//             }
//         } else {
//             console.log(`${item} does not exist.`)
//         }
//     }

//     console.log(stock)
// }

// myBill()

// // Exercise 3

// function changeEnough(itemPrice, amountOfChange){
    
//     const quarters = amountOfChange[0]*0.25
//     console.log(`Input ${amountOfChange[0]} quarters. Totalling ${quarters}`)
//     const dimes = amountOfChange[1]*0.10
//     console.log(`Input ${amountOfChange[1]} dimes. Totalling ${dimes}`)
//     const nickels = amountOfChange[2]*0.05
//     console.log(`Input ${amountOfChange[2]} nickels. Totalling ${nickels}`)
//     const pennys = amountOfChange[3]*0.01
//     console.log(`Input ${amountOfChange[3]} pennys. Totalling ${pennys}`)

//     const totalChange = quarters+dimes+nickels+pennys
//     console.log(`Total change: ${totalChange}`)
//     console.log(`Item price: ${itemPrice}`)

//     if (totalChange > itemPrice){
//         console.log(true)
//         return true
//     } else {
//         console.log(false)
//         return false
//     }
// }

// changeEnough(14.11, [2,100,0,0])
// changeEnough(0.75, [0,0,20,5])

// // Exercise 4

// function hotelCost(){

//     let askUserLengthOfStay = true
//     var lengthOfStay = prompt("How many nights would you like to stay?")

//     while (askUserLengthOfStay === true){
//         if (isNaN(lengthOfStay) || lengthOfStay == ""){
//             lengthOfStay = prompt("That was not a valid input, please try again. How many nights would you like to stay?")
//         } else {
//             askUserLengthOfStay = false;
//             return lengthOfStay*140
//         }
//     }

// }

// alert(`Your total cost is: $${hotelCost()}`)

// 2 - Define a function called planeRideCost().
//  - The function should return a different price depending on the location.
        //  - “London”: 183$
        //  - “Paris” : 220$
        //  - All other destination : 300$

function planeRideCost(){
    const prices = {
        london: 183,
        laris: 220
    }
    var destination = prompt("What is your destination?")

    askUserDestination = true

    while (askUserDestination){
        if (isNaN(destination) === false || destination == ""){
            destination = prompt("That was not a valid input, please try again. What is your destination?")
        } else {
            askUserDestination = false;
            alert(`User input a string of ${destination}`)

            if (prices[destination.toLowerCase]) {
                alert(prices.destination)
            }

        }
    }
}

planeRideCost()