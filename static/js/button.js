const box = document.getElementById("myCon");
const body = document.body;

function mycon() {
  box.style.display = "block";
  body.style.overflow = "hidden";
}

function closeBtn() {
  box.style.display = "none";
  body.style.overflow = "visible";
}

window.onclick = function (event) {
  if (event.target == box) {
    box.style.display = "none";
    body.style.overflow = "visible";
  }
};
