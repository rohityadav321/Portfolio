//Get the button
const mybutton = document.getElementById("myBtn");
const sec = document.getElementById("home");
const nav = document.getElementById("nav");
const logo = document.getElementById("logo");



// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.bottom = 50+"px";
    sec.style.height = 75+"px";
    nav.style.padding = 20+"px "+ 0 ;
    logo.style.marginTop = 20+"px";
    sec.style.transition = "all "+ 0.4+"s "+" ease-in-out";
    nav.style.transition = "all "+ 0.4+"s "+" ease-in-out";
    logo.style.transition = "all "+ 0.4+"s "+" ease-in-out";
  } else {
    mybutton.style.bottom = "-"+10+"%";
    sec.style.height = 100+"px";
    nav.style.padding = 30+"px "+ 0 ;
    logo.style.marginTop = 30+"px";
    sec.style.transition = "all "+ 0.4+"s "+" ease-in-out";
    nav.style.transition = "all "+ 0.4+"s "+" ease-in-out";
    logo.style.transition = "all "+ 0.4+"s "+" ease-in-out";
  }
}


// When the user clicks on the button, scroll to the top of the document
function topFunction(){
  document.documentElement.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}

// media query

// var modal = document.getElementById("myModal");

// // Get the button that opens the modal
// var btn = document.getElementById("mybtn");

// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
function myfun(pros) {
  document.getElementById("myModal-"+pros).style.display = "block";
  document.body.style.overflow="hidden";
  
}
// When the user clicks on <span> (x), close the modal
function closefun(pros) {
  document.getElementById("myModal-"+pros).style.display = "none";
  document.body.style.overflow="visible";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(pros) {
  if (pros.target == document.getElementById("myModal-"+pros)) {
    document.getElementById("myModal-"+pros).style.display = "none";
    document.body.style.overflow="visible";
  }
}
