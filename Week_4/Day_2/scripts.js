// With jQuery
$("#headerthree").click(() => {
    $(this).css({"display":"none"})
})

// Without jQuery
let h3 = document.getElementById('headerThree')
h3.addEventListener('click', function() {
    h3.style.display='none'
})