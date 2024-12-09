// // EXERCISE 1

// const url = "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
// let options = {
//     method: "GET",
//     headers: {
//         "content_type": "application/json"
//     }

// }

// async function getGif(url, options) {
//     try {
//         let result = await fetch(url,options)
//         let data = await result.json()
//         console.log(data.data[0].url)

//     } catch (err){
//         console.log(err)
//     }
// }

// getGif(url, options)

// // EXERCISE 2

// const url = "https://api.giphy.com/v1/gifs/search?q=sun&limit=10&offset=2&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
// let options = {
//     method: "GET",
//     headers: {
//         "content_type": "application/json"
//     }

// }

// async function getGif(url, options) {
//     try {
//         let result = await fetch(url,options)
//         let data = await result.json()
//         data.data.forEach(i => {
//             console.log(i.url)
//         })

//     } catch (err){
//         console.log(err)
//     }
// }

// getGif(url, options)

// // EXERCISE 3

// async function startshipsAPI() {
//     try {
//         let result = await fetch("https://www.swapi.tech/api/starships/9/", {
//             method: "GET",
//             headers: {
//                 "content_type": "application/json"
//             }
//         })
//         let data = await result.json()
    
//         console.log(data.result)
//     } catch (err) {
//         console.log(err)
//     }
// }

// startshipsAPI()

// EXERCISE 4

function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();

// OUTPUT: 'calling' 2 second delay and then 'resolved'