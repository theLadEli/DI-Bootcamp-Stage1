let formattedGifs = {}

async function getRelevantGif(event) {
    event.preventDefault()
    const category = $("#category").val()

    const result = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${category}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)

    const data = await result.json()
    const gifURL = data.data.images.original.url
    console.log(`Gif URL: ${gifURL}`)
    const gifID = data.data.id
    console.log(`Gif ID: ${gifID}`)

    console.log(formattedGifs)
    formattedGifs[gifID] = `<div id="${gifID}"><img src="${gifURL}"><button onclick="deleteGif('${gifID}')">Delete</button></div>`
    console.log(formattedGifs)

    regenerateGifGrid()
}

function deleteGif(gifID){
    delete formattedGifs[gifID]
    regenerateGifGrid()
}

function deleteAllGifs() {
    formattedGifs = {}
    regenerateGifGrid()
}

function regenerateGifGrid() {
    const gridHTML = Object.values(formattedGifs).join("");
    $("#grid-of-gifs").html(gridHTML);
}

$("form").on("submit", getRelevantGif)