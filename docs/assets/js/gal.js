const buttons = document.querySelectorAll('.project');
const overlay = document.querySelector('.overlay');
const overlayImage = document.querySelector('.overlay-inner img');
function open(e){
    overlay.classList.add('open');
    const src = e.currentTarget.querySelector('img').src;
    overlayImage.src = src;
}
function close(){
    overlay.classList.remove('open');
}
    buttons.forEach(button => button.addEventListener('click', open));
    overlay.addEventListener('click', close);
