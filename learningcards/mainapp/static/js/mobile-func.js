const burgerButtonBox = document.querySelector(".burger-button__content");
const burgerButton = burgerButtonBox.querySelector("button");
const principalMenu = document.getElementById("principal__menu");

const userButtonNavbar = document.querySelector('.user-navbar__li');
const kitButtonNavbar = document.querySelector('.kit-navbar__li');

const submenusUser = document.querySelector(".user-navbar__li--options");
const submenusKit = document.querySelector(".kit-navbar__li--options");

const sidebarButtonBox = document.querySelector(".sidebar-button__content");
const sidebarButton = document.querySelector(".sidebar-button__content button");
const sidebarMenu = document.getElementById("sidebar__menu");

const main = document.querySelector('main');

let prevPositionStyle;

function submenusCollapse(){
    submenusUser?.classList.remove("visible");
    submenusKit?.classList.remove("visible");
}

function showOrCollapsePrincipalMenu() {
    burgerButtonBox.classList.toggle("burger-button__content--show");
    if (principalMenu.style.display === "") {
        principalMenu.style.display = "flex";
        prevPositionStyle = document.querySelector('body > header').style.position;
        document.querySelector('body > header').style.position = "fixed";
        burgerButton.classList.remove("icon-menu3");
        burgerButton.classList.add("icon-menu4");
        if (localStorage.getItem("sidebarMenuShow") === "yes") {
            showOrCollapseSidebarMenu();
        }
        localStorage.setItem("principalMenuShow", "yes");
    } else {
        principalMenu.style.display = null;
        if (prevPositionStyle === "fixed") {
            document.querySelector('body > header').style.position = null;
        } else {
            document.querySelector('body > header').style.position = prevPositionStyle;
        }
        burgerButton.classList.remove("icon-menu4");
        burgerButton.classList.add("icon-menu3");
        submenusCollapse();
        localStorage.setItem("principalMenuShow", "no");
    }
}

function showOrCollapseSidebarMenu() {
    sidebarButtonBox.classList.toggle("sidebar-button__content--show")
    if (sidebarMenu.style.display === "") {
        sidebarMenu.style.display = "flex";
        prevPositionStyle = document.querySelector('body > header').style.position;
        document.querySelector('body > header').style.position = "fixed";
        if (localStorage.getItem("principalMenuShow") === "yes") {
            showOrCollapsePrincipalMenu();
        }
        localStorage.setItem("sidebarMenuShow", "yes");
    } else {
        sidebarMenu.style.display = null;
        if (prevPositionStyle === "fixed") {
            document.querySelector('body > header').style.position = null;
        } else {
            document.querySelector('body > header').style.position = prevPositionStyle;
        }
        localStorage.setItem("sidebarMenuShow", "no");
        if (screen.width > 650) {
            submenusCollapse();
        }
    }
}



burgerButton.addEventListener("click", showOrCollapsePrincipalMenu);

if (userButtonNavbar !== null){
    userButtonNavbar.addEventListener("click", () => {
        submenusUser.classList.toggle("visible");
        if (screen.width > 650) {
            submenusKit.classList.remove("visible");
        }
    })
}

if (kitButtonNavbar !== null){
    kitButtonNavbar.addEventListener("click", () => {
        submenusKit.classList.toggle("visible");
        if (screen.width > 650) {
            submenusUser.classList.remove("visible");
        }
    })
}

if (sidebarButton !== null){
    sidebarButton.addEventListener("click", showOrCollapseSidebarMenu);
}

main.addEventListener('click', () => {
    submenusCollapse();
})