const dialogButtons = document.getElementsByClassName("dialog__button");
const dialogModals = document.getElementsByClassName("modal");
const closeButtonsModal = document.getElementsByClassName("modal__button--close");

function showDialog(event){
    let sign = '__button--show-dialog';
    for (let className of event.target.classList) {
        if (className.endsWith(sign)){
            let dialogModal = document.getElementsByClassName(className.replace(sign, '__modal'))[0];
            dialogModal.showModal();
        }
    }
    document.body.classList.add("modal-open");
}

function externalCloseDialog(event){
    if (event.target.tagName === "DIALOG") {
        event.target.close();
        document.body.classList.remove("modal-open");
    }
}

function closeModal(event){
    event.target.parentElement.close()
    document.body.classList.remove("modal-open");
}

function initialDialogEvents(){
    for (let dialogButton of dialogButtons) {
        dialogButton.addEventListener('click', showDialog);
    }
    
    for (let dialogModal of dialogModals) {
        dialogModal.addEventListener('click', externalCloseDialog);
    }

    for (let closeButtonModal of closeButtonsModal) {
        closeButtonModal.addEventListener('click', closeModal);
    }
}

initialDialogEvents();
