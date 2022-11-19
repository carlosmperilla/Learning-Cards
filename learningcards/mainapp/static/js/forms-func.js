const csrftoken_login = getCookie('csrftoken');
const csrftoken_signup = getCookie('csrftoken');
const csrftoken_guests = getCookie('csrftoken');

const loginForm = document.getElementById('form__login');
const loginFormButtonSubmit = document.querySelector('.logIn__modal button[type="submit"]');
const loginFormErrorBox = document.querySelector('.logIn__modal .form__error-box');

const signupForm = document.getElementById('form__signup');
const signupFormButtonSubmit = document.querySelector('.signUp__modal button[type="submit"]');
const signupFormErrorBox = document.querySelector('.signUp__modal .form__error-box');

const guestsForm = document.getElementById('form__guests');
const guestsButton = document.querySelector('.guests__button');

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

function loginAjax(){
    let form = new FormData(loginForm);
    form.append('lc-lang', localStorage.getItem('lc-lang'));
    const request = new Request(
        url_login,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken_login,
            },
            body: form,
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        if (content.hasOwnProperty('invalid')){
           loginFormErrorBox.innerText =  content.invalid;
           loginFormErrorBox.classList.add('visible');
        } else {
            loginFormErrorBox.classList.remove('visible');
            window.location.href = content.redirect_url;
        }

        })()
}

function loginGuestsAjax(){
    let form = new FormData(guestsForm);
    form.append('lc-lang', localStorage.getItem('lc-lang'));
    const request = new Request(
        url_login,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken_guests,
            },
            body: form,
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        window.location.href = content.redirect_url;

        })()
}

function humanizeSignupFieldErrors(errors){
    let plc_username = signupForm.querySelector('input[name="username"]').placeholder;
    let plc_email = signupForm.querySelector('input[name="email"]').placeholder;
    let plc_password1 = signupForm.querySelector('input[name="password1"]').placeholder;
    let plc_password2 = signupForm.querySelector('input[name="password2"]').placeholder;
    
    errors = errors.replace('username', `<span class="title__error">${plc_username}</span>`);
    errors = errors.replace('email', `<span class="title__error">${plc_email}</span>`);
    errors = errors.replace('password1', `<span class="title__error">${plc_password1}</span>`);
    errors = errors.replace('password2', `<span class="title__error">${plc_password2}</span>`);
    return errors
}

function signupAjax(){
    let form = new FormData(signupForm);
    form.append('lc-lang', localStorage.getItem('lc-lang'));
    const request = new Request(
        url_signup,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken_signup,
            },
            body: form,
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        if (content.hasOwnProperty('errors')){
           signupFormErrorBox.innerHTML =  humanizeSignupFieldErrors(content.errors);
           signupFormErrorBox.classList.add('visible');
        } else {
            signupFormErrorBox.classList.remove('visible');
            window.location.href = content.redirect_url;
        }

        })()
}

function validateLoginForm(event){
    event.preventDefault();
    if (loginForm.checkValidity()){
        loginFormErrorBox.classList.remove('visible');
        loginAjax();
    } else {
        loginForm.reportValidity();
    }
}

function validateSignupForm(event){
    event.preventDefault();
    if (signupForm.checkValidity()){
        signupFormErrorBox.classList.remove('visible');
        signupAjax();
    } else {
        signupForm.reportValidity();
    }
}

loginFormButtonSubmit.addEventListener("click", validateLoginForm);
signupFormButtonSubmit.addEventListener("click", validateSignupForm);
guestsButton.addEventListener("click", loginGuestsAjax);
