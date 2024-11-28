// With jQuery
$("#headerthree").click(function() {
    $(this).css("display","none")
})

// Without jQuery
let h3 = document.getElementById('headerThree')
h3.addEventListener('click', function() {
    h3.style.display='none'
})