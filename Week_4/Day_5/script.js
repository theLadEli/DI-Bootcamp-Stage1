$("input").each(function() {
    const color = $(this).val();
    $(this).css("background-color",color)
})

$(window).on("load",function(){
    const squaresWidth = $("#squares").width()
    const squaresHeight = $("#squares").height()
    const totalRows = squaresHeight/22
    const squaresPerRow = squaresWidth/22
    // alert(`Width: ${squaresHeight}\nHeight: ${squaresHeight}`)
    const totalSquaresToAppend = (squaresHeight*squaresWidth)/(22*22)

    // Loop to amount of needed rows
    for (let i = 0; i < totalRows; i++) {
        $("#squares").append(`
            <div class="square-row">${
                for (let e = 0; e < squaresPerRow; e++){
                    `<div class="color-square"></div>`
                }
            }</div>`)
    }

    // for(let i = 0; i < totalSquaresToAppend; i++) {
    //     $("#squares").append(`<div class="color-square"></div>`)
    // }
})