const deleteKitButtonSide = document.querySelector(".delete__button--sidebar-action");
const finalDeleteKitButton = document.querySelector(".kit__button--delete");
const csrftoken_deleteKit = getCookie('csrftoken');

let kitsToDelete = new Set(); 

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function deleteTracking(event){
    let kitContent = event.target.closest('.kit__content');

    if (event.target.checked) {
        kitsToDelete.add(kitContent.id);
    } else {
        kitsToDelete.delete(kitContent.id);
    }
}

function removeEditActions(kitBox){
    let kitName = kitBox.querySelector('.kit__content__name h3');
    let kitForeignLanguage = kitBox.querySelector('.kit__content__languages--foreign');
    let kitNativeLanguage = kitBox.querySelector('.kit__content__languages--native');
    let editableElements = [kitName, kitForeignLanguage, kitNativeLanguage];

    for (let element of editableElements) {
        element.contentEditable = false;
        element.classList.remove('kit-value--editable');
        element.removeEventListener("input", editTracking);
    }
}

function makeDeleteKitBox(kitBox){
    let kitDeleteCheckbox = kitBox.querySelector('.kit__item--delete-content input[type="checkbox"]');
    
    kitDeleteCheckbox.closest('.kit__item--delete-content').classList.add('visible');
    kitDeleteCheckbox.addEventListener("click", deleteTracking);

    removeEditActions(kitBox);
}

function activeKitDeleteMode() {
    for (let kitContent of kitContents){
        makeDeleteKitBox(kitContent);
    }
    mainContentKits.classList.add('action-button-space');
    finalDeleteKitButton.classList.add("visible");
    finalEditKitButton.classList.remove("visible");

    showOrCollapseSidebarMenu();
}

function sendkitsToDelete(){
    let kitsToDeletePack = {'kitsToDelete': [...kitsToDelete], 'lc-lang' : localStorage.getItem("lc-lang")};
    const request = new Request(
        url_deleteKit,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken_deleteKit,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(kitsToDeletePack),
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        if (content.hasOwnProperty('redirect_url')) {
            window.location.href = content.redirect_url;
        } else {
            let erroMessage = (localStorage.getItem("lc-lang") === "es") && 
                              "No se ha podido eliminar correctamente, revise su conexion a internet y recargue la pagina." ||
                              "Could not delete correctly, check your internet connection and reload the page.";

            window.alert(erroMessage);
        }    
    })()
}

function confirmDelete(){
    let countkitsToDelete = kitsToDelete.size.toString();
    let msgConfirm = (localStorage.getItem("lc-lang") === "es") && "¿Quiere eliminar " + countkitsToDelete + " elementos?" ||
                    "Do you want to remove " + countkitsToDelete + " items?";

    if (window.confirm(msgConfirm) && (kitsToDelete.size > 0)) {
            sendkitsToDelete()
    }
}

deleteKitButtonSide.addEventListener("click", activeKitDeleteMode);
finalDeleteKitButton.addEventListener("click", confirmDelete);
