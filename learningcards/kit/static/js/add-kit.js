const addKitFinalButton = document.querySelector('.addKit__final-button');
const addKitForm = document.querySelector('#form__addKit');
const inputFile = addKitForm.querySelector('input[name="kit_file"]');
const langAddKitForm = addKitForm.querySelector("input[name='lc-lang']")


inputFile.addEventListener("change", (event) => {
    if (addKitForm.checkValidity()){
        langAddKitForm.value = localStorage.getItem('lc-lang');
        addKitForm.submit();
        event.preventDefault();
        addKitFinalButton.setAttribute('disabled', true);
        addKitFinalButton.style.filter = "grayscale(1)";
    } else {
        addKitForm.reportValidity();
    }
})

addKitFinalButton.addEventListener("click", () => {
    inputFile.click();
})