// 1. Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// 2. The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

((numChildren, partnerName, location, jobTitle) => {
    document.getElementById("main").append(`You will be a ${jobTitle} in ${location}, and married to ${partnerName} with ${numChildren} kids.`)
})(4, "Steve","Tel Aviv", "Web Developer")