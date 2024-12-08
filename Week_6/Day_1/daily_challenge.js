let arrayOfWords = ['random', 'cheese', 'eggs', 'table']

function makeAllCaps(arrayOfWords) {
    return new Promise((resolve, reject) => {
        
        if (arrayOfWords.every(item => typeof item === "string")) {
            resolve(arrayOfWords.map(item => item.toUpperCase()))
        } else {
            reject("Not all items in the array are uppercase.")
        }

    })
}

const makeArrayAllCaps = makeAllCaps(arrayOfWords)

function sortWords(arrayOfWords) {
    return new Promise((resolve, reject) => {

        if (arrayOfWords.length >= 4){
            resolve(arrayOfWords.sort())
        } else (
            reject("More then four words in the array.")
        )

    })
}

makeAllCaps(arrayOfWords)
    .then(uppercaseWords => {
        console.log("Uppercased:", uppercaseWords);
        return sortWords(uppercaseWords);
    })
    .then(sortedWords => {
        console.log("Sorted:", sortedWords);
    })
    .catch(error => {
        console.log("Error:", error);
    });
