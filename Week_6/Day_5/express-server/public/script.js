const url = "http://localhost:3003/users"
let options = {
    method: "GET",
    headers: {
        "content_type": "application/json"
    }

}

async function getUsers(url, options) {
    try {
        let result = await fetch(url,options)
        let data = await result.json()
        data.forEach(user => {
            $("#users").append(`Name: ${user.name} | Email: ${user.email}<br>`)
        })

    } catch (err){
        console.log(err)
    }
}

getUsers(url, options)