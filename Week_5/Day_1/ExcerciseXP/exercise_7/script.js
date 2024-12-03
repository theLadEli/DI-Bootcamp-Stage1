(username => {
    $("#user-info").append(`
        <img src="${username}.png">
        <p>${username}</p>
    `)
})("Eli")