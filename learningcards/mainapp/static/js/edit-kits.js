const mainContentKits = document.querySelector('.main__content__kits');
const kitContents = document.getElementsByClassName("kit__content");
const editKitButtonSide = document.querySelector(".edit__button--sidebar-action");
const finalEditKitButton = document.querySelector(".kit__button--edit");
const csrftoken_editKit = getCookie('csrftoken');

let kitEdited = {}; 

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


function editTracking(event){
    let kitContent = event.target.closest('.kit__content');
    let kitField = event.target.classList.contains("kit__content__languages--foreign") && "foreign_language" ||
                   event.target.classList.contains("kit__content__languages--native") && "native_language" ||
                   "name";

    if (!kitEdited.hasOwnProperty(kitContent.id)){
        kitEdited[kitContent.id] = {};
    }
    kitEdited[kitContent.id][kitField] = event.target.innerText;
}

function removeDeleteActions(kitBox){
    let kitDeleteCheckbox = kitBox.querySelector('.kit__item--delete-content input[type="checkbox"]');
    
    kitDeleteCheckbox.closest('.kit__item--delete-content').classList.remove('visible');
    kitDeleteCheckbox.removeEventListener("click", deleteTracking);
}

function makeEditableKitBox(kitBox){
    let kitName = kitBox.querySelector('.kit__content__name h3');
    let kitForeignLanguage = kitBox.querySelector('.kit__content__languages--foreign');
    let kitNativeLanguage = kitBox.querySelector('.kit__content__languages--native');
    let editableElements = [kitName, kitForeignLanguage, kitNativeLanguage];

    for (let element of editableElements) {
        element.contentEditable = true;
        element.classList.add('kit-value--editable');   
        element.addEventListener("input", editTracking);
    }

    removeDeleteActions(kitBox);
}

function activeKitEditMode() {
    for (let kitContent of kitContents){
        makeEditableKitBox(kitContent);
    }
    mainContentKits.classList.add('action-button-space');
    finalEditKitButton.classList.add("visible");
    finalDeleteKitButton.classList.remove("visible");

    showOrCollapseSidebarMenu();
}

function sendKitEdited(){
    kitEdited['lc-lang'] = localStorage.getItem("lc-lang");
    const request = new Request(
        url_editKit,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken_editKit,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(kitEdited),
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
                              "No se ha podido editar correctamente, revise su conexion a internet y recargue la pagina." ||
                              "Could not edit correctly, check your internet connection and reload the page.";

            window.alert(erroMessage);
        }    
    })()
}

function confirmEdit(){
    if (JSON.stringify(kitEdited) !== "{}") {
        sendKitEdited();
    } else {
        let erroMessage = (localStorage.getItem("lc-lang") === "es") && 
        "Falta editar elementos." ||
        "Missing edit elements.";

        window.alert(erroMessage);
    }
}

editKitButtonSide.addEventListener("click", activeKitEditMode);
finalEditKitButton.addEventListener("click", confirmEdit);
