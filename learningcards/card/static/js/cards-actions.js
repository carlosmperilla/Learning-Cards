const showNativeWordButtons = document.querySelectorAll('.card__content__foreign-word button');
const replaceImgButtons = document.querySelectorAll('.card--renew-img');
const validateWordButtons = document.querySelectorAll('.validate-word__final-button');
const kitProgress = document.querySelector('.kit__info__progress--value');
const randomizeButton = document.querySelector('.randomize-button__content button');

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


function sendAjaxRequest(url, jsonObj, func, event){
    const request = new Request(
        url,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonObj),
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        func(event, content);
    })()
}

function setNativeWord(event, content){
    let cardContent = event.target.closest('.card__content');
    let cardContentForeigWordPanel = cardContent.querySelector('.card__content__foreign-word');
    let cardContentTitle = cardContent.querySelector('.card__content__foreign-word h3');

    if (content.hasOwnProperty('native_word')) {
        let foreginWord = cardContentTitle.innerText;
        cardContentTitle.innerText = content.native_word;
        cardContentForeigWordPanel.style.filter = "grayscale(1)";
        event.target.disabled = true;
        setTimeout(() => {
            cardContentTitle.innerText = foreginWord;
            cardContentForeigWordPanel.style.filter = null;
            event.target.disabled = false;
        }, 3000);
    } else {
        let erroMessage = (localStorage.getItem("lc-lang") === "es") && 
                          "Error en revelar, revise su conexion a internet y recargue la pagina." ||
                          "Error in revealing, check your internet connection and reload the page.";

        window.alert(erroMessage);
    }
}

function getAndSetNativeWord(event){
    let cardContent = event.target.closest('.card__content');
    let jsonObj = {card_id: cardContent.id};
    sendAjaxRequest(url_showNativeWord, jsonObj, setNativeWord, event);
}

function changeImg(event, content){
    let cardContent = event.target.closest('.card__content');
    let cardContentRenewImg = cardContent.querySelector('.card--renew-img');
    let cardContentImg = cardContent.querySelector('.card__content__img img');

    if (content.hasOwnProperty('url_img')) {
        cardContentImg.src = content.url_img;
        cardContentRenewImg.disabled = true;
        cardContentRenewImg.style.filter = "grayscale(1)";
        setTimeout(() => {
            cardContentRenewImg.disabled = false;
            cardContentRenewImg.style.filter = null;
        }, 1000);
    } else {
        let erroMessage = (localStorage.getItem("lc-lang") === "es") && 
                          "Error en remplazar imagen, revise su conexion a internet y recargue la pagina." ||
                          "Error in replace image, check your internet connection and reload the page.";

        window.alert(erroMessage);
    }
}

function replaceImg(event){
    let cardContent = event.target.closest('.card__content');
    let jsonObj = {card_id: cardContent.id};
    sendAjaxRequest(url_replaceImg, jsonObj, changeImg, event);
}

function checkWords(event, content){
    let cardContent = event.target.closest('.card__content');
    let cardContentInput = cardContent.querySelector('input[name="native_word"]')
    let cardState = cardContent.querySelector('.card__state');
    let cardHits = cardContent.querySelector('.card__content__score--hits-value span');
    let cardMistakes = cardContent.querySelector('.card__content__score--mistakes-value span');

    if (content.hasOwnProperty('passed')) {
        if (content.passed){
            cardState.classList.remove('icon-wondering2', 'icon-confused2', 'fail');
            cardState.classList.add('icon-grin2', 'success');
            cardHits.innerText = content.hits;
        } else {
            cardState.classList.remove('icon-wondering2', 'icon-grin2', 'success');
            cardState.classList.add('icon-confused2', 'fail');
            cardMistakes.innerText = content.mistakes;
        }
        cardContentInput.value = "";
        kitProgress.innerText = content.progress;
    } else {
        let erroMessage = (localStorage.getItem("lc-lang") === "es") && 
                          "Error en chequear palabra, revise su conexion a internet y recargue la pagina." ||
                          "Error in validate word, check your internet connection and reload the page.";

        window.alert(erroMessage);
    }
}

function validateWord(event){
    event.preventDefault();
    let cardContent = event.target.closest('.card__content');
    let cardContentInput = cardContent.querySelector('input[name="native_word"]');
    if (cardContentInput.value === "") {
        return null
    }
    let jsonObj = {
                    card_id: cardContent.id,
                    native_word: cardContentInput.value
                };
    sendAjaxRequest(url_validateWord, jsonObj, checkWords, event);
}

function randomizeCard(event){
    sendAjaxRequest(url_randomizeKit, {}, (e, content) => {
        if (content.hasOwnProperty('randomized')) {
            location.reload();
        } else {
            let erroMessage = (localStorage.getItem("lc-lang") === "es") && 
            "Error en mezclar tarjetas, revise su conexion a internet y recargue la pagina." ||
            "Error in shuffle cards, check your internet connection and reload the page.";

            window.alert(erroMessage);
        }
    }, event);
}

for (let showNativeWordButton of showNativeWordButtons) {
    showNativeWordButton.addEventListener("click", getAndSetNativeWord);
}

for (let replaceImgButton of replaceImgButtons) {
    replaceImgButton.addEventListener("click", replaceImg);
}

for (let validateWordButton of validateWordButtons) {
    validateWordButton.addEventListener("click", validateWord);
}

randomizeButton.addEventListener("click", randomizeCard);