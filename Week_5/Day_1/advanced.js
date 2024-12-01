// Create a function to check the year given by the user
// If the year is after 2000, you should display "You are in the 21st century", else you should display "You live in the Middle Age"

function checkYear(year){

    var middleAge = false

    if (year < 2000){
        middleAge = false
    } else {
        middleAge = true
    }

    return(middleAge ? "You are in the 21st century" : "You live in the middle age")
}

console.log(checkYear(2100))