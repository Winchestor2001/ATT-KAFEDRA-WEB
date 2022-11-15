let leftBtn = document.querySelector(".left_btn")
let links = document.querySelector('.left_content')
let right_content = document.querySelector('.right_content')
leftBtn.addEventListener('click', (e) => {
  links.classList.toggle("left_active")
  right_content.classList.toggle('right_active')
});

let get_file = document.querySelector(".profile_logo");
let get_file_input = document.querySelector("#get_file_input");
get_file.onclick = () => {
  get_file_input.click();
};
function clickInput() {
  let send_file_btn = document.querySelector("#send_ava");
  send_file_btn.submit();
}
const liClick = document.querySelectorAll('.drop_a')
liClick.forEach(element => {
  element.addEventListener('click', () => {
    element.nextElementSibling.classList.toggle('active')
  })
});


function showNotic(color){
  let notic = document.querySelector('.Message')
  let notic_color = document.querySelector('.Message--green')
  notic.style.display = 'block'
  notic_color.style.background = color
  setTimeout(() => {
    notic.style.display = 'none'
  }, 2000)
}







