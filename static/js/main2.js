let right_top_btn = document.querySelector('.right_toper_btn');

right_top_btn.onclick = () => {
    document.documentElement.scrollTop = 0;
}

window.onscroll = () => {
  if (window.pageYOffset > 400) {
    right_top_btn.classList.add('active3');
  }
  else{
    right_top_btn.classList.remove('active3');
  }
}


window.onload = () => {
    let loader = document.querySelector("#preloader");
//    loader.style.display = 'none';
     loader.style.opacity = 0;
     loader.style.visibility = "hidden";
  };


