(username => {
    $("#user-info").append(`
        <img src="${username}.png" id="pfp">
        <p>${username} →</p>
    `)
})("Eli")