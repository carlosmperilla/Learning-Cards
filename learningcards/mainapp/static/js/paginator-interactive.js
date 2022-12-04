const datalistPages = document.getElementById('kit-pages__datalist');
const inputPageAll = document.querySelectorAll('input[list="kit-pages__datalist"]');
const paginatorAll = document.getElementsByClassName('kit__pagination');

let currentUrl = new URL(window.location.href);
let nPagesShown;
let currentPage;

function setNPagesShown(){
    nPagesShown = (screen.width < 700) && 3 ||
    (screen.width < 900) && 5 ||
    (screen.width < 1400) && 9 ||
    15
}

function paginatorRecompose(){
    let prevNPagesShown = nPagesShown;
    setNPagesShown();

    if (prevNPagesShown !== nPagesShown){
        for (let paginator of paginatorAll){
            let rowElements = paginator.getElementsByClassName('kit__pagination--row');
            let persistentRowElements = [];
            for (let rowElement of rowElements){
                persistentRowElements.push(rowElement.cloneNode(true));
            }
            paginator.replaceChildren();
            paginator.append(...persistentRowElements);
        }
        fillPaginator(paginatorAll);
    }

}

function createLinkPage(num_page) {
    let linkPage = document.createElement('a');
    linkPage.innerHTML = num_page;
    currentUrl.searchParams.set('page', num_page);
    linkPage.href = currentUrl.href;
    return linkPage
}

function fillPaginator(paginators){
    let firstPage = 1;
    let prev_pages = Math.max(currentPage - Math.floor(nPagesShown/2), firstPage);
    let next_pages = Math.min(currentPage + Math.floor(nPagesShown/2), numPages);
    let elements = [];

    for (num_page = prev_pages; num_page < currentPage; num_page++){
        prevLinkPage = createLinkPage(num_page);
        elements.push(prevLinkPage);
    }

    currentLinkPage = createLinkPage(currentPage);
    currentLinkPage.classList.add('active');
    elements.push(currentLinkPage);
    
    for (num_page = currentPage + 1; num_page <= next_pages; num_page++){
        nextLinkPage = createLinkPage(num_page);
        elements.push(nextLinkPage);
    }
    
    for (let paginator of paginators){
        a = paginator.append(...elements.map(node => node.cloneNode(true)));
    }
}

setNPagesShown();
window.onresize = paginatorRecompose;

if (currentUrl.searchParams.get('page') === null){
    currentPage = 1;
} else {
    currentPage = parseInt(currentUrl.searchParams.get('page'));
}

for (let numPage=1; numPage<=numPages; numPage++){
    let option = document.createElement('option');
    option.value = numPage;
    datalistPages.appendChild(option);
}

for (let inputPage of inputPageAll){
    inputPage.addEventListener("change", (e) => {
        currentUrl.searchParams.set('page', e.target.value);
        window.location.href = currentUrl.href;
    })
}

fillPaginator(paginatorAll);