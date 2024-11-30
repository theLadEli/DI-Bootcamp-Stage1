var selectedColor = ''
var mousePress = false

$("input").each(function() {
    selectedColor = $(this).val();
    $(this).css("background-color",selectedColor)
    $(this).css("color",selectedColor)
})

$(window).on("load",function(){
    const squaresHeight = $("#squares").height()
    const totalRows = squaresHeight/22
    const squaresWidth = $("#squares").width()
    const squaresPerRow = squaresWidth/22
    let rowOfSquares = '<div class="color-square"></div>'.repeat(squaresPerRow)

    for (let i = 0; i < totalRows; i++) {
        $("#squares").append(`
            <div class="square-row">${rowOfSquares}</div>
        `)
    }

    $(".color-picker").click(function() {
        selectedColor = $(this).val();
    })

    $(".color-square").on("mousedown", function () {
        mousePress = true;
        $(this).css("background-color",selectedColor)
    });

    $(".color-square").on("mouseenter", function () {
        if (mousePress) {
            $(this).css("background-color",selectedColor)
        }
    });

    $(document).on("mouseup", function () {
        mousePress = false;
    });

})

function clearBoard() {
    $(".color-square").each(function() {
        selectedColor = "white"
        $(this).css("background-color",selectedColor)
    })
}