var red_header = document.getElementById('red_header')

red_header.addEventListener('click', function(){
    var header = document.querySelector('header');
    header.classList.add("red");
})
