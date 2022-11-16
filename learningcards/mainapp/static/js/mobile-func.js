const burgerButtonBox = document.querySelector(".burger-button__content");
const burgerButton = burgerButtonBox.querySelector("button");
const principalMenu = document.getElementById("principal__menu");


function showOrCollapseMenu(){
    burgerButtonBox.classList.toggle("burger-button__content--show");
    console.log(principalMenu.style.display)
    if (principalMenu.style.display === "") {
        principalMenu.style.display = "flex";
    } else {
        principalMenu.style.display = null;
    }
}


burgerButton.addEventListener("click", showOrCollapseMenu);