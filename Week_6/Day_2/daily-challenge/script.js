async function getRelevantGif(event) {
    event.preventDefault()
    const category = document.getElementById("category").value

    const result = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${category}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)

    const data = await result.json()
    const gifURL = data.data.images.original.url
    console.log(gifURL);
    

    document.querySelector("img").src = gifURL
}

document.querySelector("form").addEventListener("submit", getRelevantGif)