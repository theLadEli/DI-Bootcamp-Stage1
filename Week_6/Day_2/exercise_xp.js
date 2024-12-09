const url = "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
let options = {
    method: "GET",
    headers: {
        "content_type": "application/json"
    }

}

async function getGif(url, options) {
    try {
        let result = await fetch(url,options)
        let data = await result.json()
        console.log(data.data[0].url)

    } catch (err){
        console.log(err)
    }
}

getGif(url, options)