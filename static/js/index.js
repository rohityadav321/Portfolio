//Get the button
const mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.bottom = 50+"px";
  } else {
    mybutton.style.bottom = "-"+10+"%";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction(){
  document.documentElement.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
function home() {
  document.documentElement.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
var x= window.matchMedia("(max-width:650px)");
var y=window.matchMedia("(min-width:651px) and (max-width:900px)");

function about() {
  if(y.matches){
    document.documentElement.scrollTo({
      top: 430,
      behavior: "smooth",
    });
  }
  else if(x.matches){
    document.documentElement.scrollTo({
      top: 480,
      behavior: "smooth",
    });
  }
  else{
    document.documentElement.scrollTo({
      top: 570,
      behavior: "smooth",
    });
  }
}
function edu() {
  if(y.matches){
    document.documentElement.scrollTo({
      top: 1040,
      behavior: "smooth",
    });
  }
  else{
    document.documentElement.scrollTo({
      top: 1000,
      behavior: "smooth",
    });
  }
}function skill() {
  if(y.matches){
    document.documentElement.scrollTo({
      top: 1750,
      behavior: "smooth",
    });
  }
  else{
    document.documentElement.scrollTo({
      top: 1670,
      behavior: "smooth",
    });
  }
}
function pro() {
  if(y.matches){
    document.documentElement.scrollTo({
      top: 3340,
      behavior: "smooth",
    });
  }
  else{
    document.documentElement.scrollTo({
      top: 3300,
      behavior: "smooth",
    });
  }
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
}

// When the user clicks on <span> (x), close the modal
function closefun(pros) {
  document.getElementById("myModal-"+pros).style.display = "none";
  
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(pros) {
  if (pros.target == document.getElementById("myModal-"+pros)) {
    document.getElementById("myModal-"+pros).style.display = "none";
 
  }
}
