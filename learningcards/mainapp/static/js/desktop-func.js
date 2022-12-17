const userLiNav = document.querySelector('.user-navbar__li');
const kitLiNav = document.querySelector('.kit-navbar__li');

function enterToClick(element, clickElement){
    element.addEventListener('keyup', (event) => { 
        if (event.key == "Enter"){clickElement.click()}
    })
}

if (userLiNav !== null) {
    enterToClick(userLiNav, userLiNav);
}
if (kitLiNav !== null) {
    enterToClick(kitLiNav, kitLiNav);
}