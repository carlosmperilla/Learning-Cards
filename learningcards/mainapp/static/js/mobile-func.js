const burgerButtonBox = document.querySelector(".burger-button__content");
const burgerButton = burgerButtonBox.querySelector("button");
const principalMenu = document.getElementById("principal__menu");

const userButtonNavbar = document.querySelector('.user-navbar__li');
const kitButtonNavbar = document.querySelector('.kit-navbar__li');

const submenusUser = document.querySelector(".user-navbar__li--options");
const submenusKit = document.querySelector(".kit-navbar__li--options");

let prevPositionStyle;

function submenusCollapse(){
    submenusUser.classList.remove("visible");
    submenusKit.classList.remove("visible");
}

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
        submenusCollapse();
    }
}


burgerButton.addEventListener("click", showOrCollapseMenu);

if (userButtonNavbar !== null){
    userButtonNavbar.addEventListener("click", () => {
        submenusUser.classList.toggle("visible");
    })
}

if (kitButtonNavbar !== null){
    kitButtonNavbar.addEventListener("click", () => {
        submenusKit.classList.toggle("visible");
    })
}