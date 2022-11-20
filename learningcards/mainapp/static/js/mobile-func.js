const burgerButtonBox = document.querySelector(".burger-button__content");
const burgerButton = burgerButtonBox.querySelector("button");
const principalMenu = document.getElementById("principal__menu");

let prevPositionStyle;

function showOrCollapseMenu(){
    burgerButtonBox.classList.toggle("burger-button__content--show");
    if (principalMenu.style.display === "") {
        principalMenu.style.display = "flex";
        prevPositionStyle = document.querySelector('body > header').style.position;
        document.querySelector('body > header').style.position = "fixed";
        burgerButton.classList.remove("icon-menu3");
        burgerButton.classList.add("icon-menu4");
    } else {
        principalMenu.style.display = null;
        document.querySelector('body > header').style.position = prevPositionStyle;
        burgerButton.classList.remove("icon-menu4");
        burgerButton.classList.add("icon-menu3");
    }
}


burgerButton.addEventListener("click", showOrCollapseMenu);