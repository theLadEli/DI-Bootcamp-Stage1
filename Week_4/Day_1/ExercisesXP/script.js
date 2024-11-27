// // EXERCISE 1

// // Remove the first name from the array
// const people = ["Greg", "Mary", "Devon", "James"];
// console.log(people)
// people.shift()
// console.log(people)

// // Removes name by index (parameters of splice: start index and end index)
// const people = ["Greg", "Mary", "Devon", "James"];
// console.log(people)
// people.splice(0,1)
// console.log(people)
// people[2] = "Jason"
// console.log(people)
// people.push("Eli")
// console.log(people)
// console.log(people.indexOf("Mary"))

// const copyOfPeople = people.slice(1,3)
// console.log(copyOfPeople)

// console.log(people.indexOf("Foo"))

// const last = people[people.length-1]
// console.log(last)

// // Part II
// for (let i = 0; i < people.length; i++) {

//     if (people[i] == "Devon") {
//         console.log(people[i])
//         break
//     }
//     else {
//         console.log(people[i])
//     }
// }

// // EXERCISE 2

// const colors = ["blue", "black", "red", "yellow", "grey"];

// for (var i = 0; i < colors.length; i++) {
//     console.log(`My #${i+1} choice is ${colors[i]}`)
// }

// // EXERCISE 3
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// let userNumber = prompt("Insert a number")
// console.log(typeof(userNumber))
// Convert string to num
// userNumber = Number(userNumber)

// while (userNumber < 10) {
//     userNumber = Number(prompt("Your number is smaller then 10. Please input a new number."))
// }

// // EXERCISE 4
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// console.log(`Total number of floors: ${building.numberOfFloors}`)
// console.log(`Num apartments on floor 1: ${building.numberOfAptByFloor.firstFloor}\nNum aparments on floor 3: ${building.numberOfAptByFloor.thirdFloor}`)
// console.log(`The second tenant is ${building.nameOfTenants[1]} and they have ${building.numberOfRoomsAndRent.dan[1]} rooms in their apartment`)

// const sarahsRent = building.numberOfRoomsAndRent.sarah[1]
// const davidsRent = building.numberOfRoomsAndRent.david[1]
// const dansRent = building.numberOfRoomsAndRent.dan[1]
// console.log(davidsRent + sarahsRent)

// if (davidsRent + sarahsRent > dansRent) {
//     building.numberOfRoomsAndRent.dan[1] = 1200
//     console.log(building.numberOfRoomsAndRent.dan[1])
// }

// // EXERCISE 5
// const family = {
//     surname: "cohen",
//     familyMembers: 11,
//     oldestMember: 28,
//     youngestMember: 10
// }

// for (let property in family){
//     console.log(`${property}: ${family[property]}`)
// }

// // EXERCISE 6
// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'reindeer'
// }

// let fullString = []

// for (let property in details){
//     fullString.push(property)
//     fullString.push(details[property])
// }

// console.log(fullString.join(" "))

// // EXERCISE 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let firstLetterOfNames = []

for (let property of names){
    firstLetterOfNames.push(property[0])
}
firstLetterOfNames.sort()
societyName = firstLetterOfNames.join("")
console.log(societyName)