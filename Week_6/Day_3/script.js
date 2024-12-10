let characters = {}
let character_id = 0
let latestCharacterId

function updatePageDetails(id) {
    console.log(characters)
    $("#name").html(characters[id].name)
    $("#gender").html(characters[id].gender)
    $("#race").html(characters[id].race)
    $("#height").html(characters[id].height)
    $("#spouse").html(characters[id].spouse)
    $("#death").html(characters[id].death)

    latestCharacterId = id
}

async function getCharacter() {

    result = await fetch(`https://the-one-api.dev/v2/character?limit=1&offset=${character_id}`, {
        method: "GET",
        headers: {
            "content_type": "application/json",
            Authorization: `Bearer ${ACCESS_TOKEN}`
        }
    })

    let data = await result.json()
    let id = data.docs[0]._id

    characters[id] = {
        name: data.docs[0].name,
        gender: data.docs[0].gender,
        race: data.docs[0].race,
        height: data.docs[0].height,
        spouse: data.docs[0].spouse,
        death: data.docs[0].death
    }

    updatePageDetails(id)
    character_id++
}

function previousCharacter() {
    const keys = Object.keys(characters);
    const currentKeysIndex = keys.indexOf(latestCharacterId);

    if (currentKeysIndex == 0) {
        console.log("Nothing prior to load.")
    } else {
        const prevKey = keys[currentKeysIndex - 1];
        updatePageDetails(prevKey);
    }
}

function nextCharacter() {
    const keys = Object.keys(characters);
    const currentKeysIndex = keys.indexOf(latestCharacterId);

    if (currentKeysIndex === keys.length - 1) {
        console.log("Nothing more to load.")
    } else {
        const nextKey = keys[currentKeysIndex + 1];
        updatePageDetails(nextKey);
    }
}