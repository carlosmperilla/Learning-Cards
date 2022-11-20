const gadgetsButtonBox = document.querySelector(".gadgets__content");
const translateButton = gadgetsButtonBox.querySelector("button");
const langOptionsText = gadgetsButtonBox.querySelectorAll(".lang-option__text");
const loginOutLik = document.querySelector(".logout__li a");

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

function getJsonTranslation(){
    const request = new Request(
        url_template_translation,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    async function query() {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        return content

        }

    return query()
}

function toggleLcLang(){
    if (localStorage.getItem('lc-lang') === 'es') {
        localStorage.setItem('lc-lang', 'en');
    } else {
        localStorage.setItem('lc-lang', 'es');
    }
}

function changeLanguage(){
    for (let langOptionText of langOptionsText){
        langOptionText.classList.toggle("lang-option__text--selected");
    }
    toggleLcLang();
    translateTemplate();
}

function translateTemplate(){
    let jsonTranslation = getJsonTranslation();
    jsonTranslation.then( (data) => {
        for (let obj of data) {
            
            let element = document.querySelector(obj.selector);
            
            if (element !== null){
                if (localStorage.getItem('lc-lang') === 'es') {
                    document.querySelector(".lang-option__es").classList.add("lang-option__text--selected");
                    document.querySelector(".lang-option__en").classList.remove("lang-option__text--selected");
                    if (element.tagName === "INPUT"){
                        element.placeholder = obj.spanish_text;
                    } else {
                        element.innerHTML = obj.spanish_text;
                    }
                } else {
                    document.querySelector(".lang-option__en").classList.add("lang-option__text--selected");
                    document.querySelector(".lang-option__es").classList.remove("lang-option__text--selected");
                    if (element.tagName === "INPUT"){
                        element.placeholder = obj.english_text;
                    } else {
                        element.innerHTML = obj.english_text;
                    }
                }
            }
            
        }
    })
}

function setDefaultLanguage(){

    if (localStorage.getItem('lc-lang') !== null){
        translateTemplate();
        return localStorage.getItem('lc-lang');
    }

    let userLang = navigator.language || navigator.userLanguage;
    userLang = userLang.split('-')[0].toLowerCase();

    if (userLang === 'es') {
        localStorage.setItem('lc-lang', 'es');
    } else {
        localStorage.setItem('lc-lang', 'en');
        translateTemplate();
    }
}

translateButton.addEventListener("click", changeLanguage);
setDefaultLanguage();

if (loginOutLik !== null) {
    loginOutLik.addEventListener("click", (event) => {
       if (localStorage.getItem('lc-lang') === "es"){
           event.target.href = event.target.href.replace("lang=en", "lang=es");
       } else {
           event.target.href = event.target.href.replace("lang=es", "lang=en");
       }
    })
}