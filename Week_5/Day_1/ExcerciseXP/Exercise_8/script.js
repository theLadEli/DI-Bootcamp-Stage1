// Part I:
function makeJuice(size) {
    size = size.toLowerCase()
    ingrediants = []

    if (size == "small" || size == "medium" || size == "large") {
        console.log('Valid input.')

        function addIngredients(ingrediantOne, ingrediantTwo, ingrediantThree) {
            ingrediants.push(ingrediantOne, ingrediantTwo, ingrediantThree)

            $("#drink-rec").html(`
                <p>The client wants a ${size} juice, containing ${ingrediantOne}, ${ingrediantTwo} and ${ingrediantThree}.</p>
            `)
        }
        addIngredients("lemon", "banana", "blueberry")

    } else {
        console.log('Inalid input.')
    }
}

makeJuice("small")

// Part II:
// 3 - Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".
// 4 - The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.