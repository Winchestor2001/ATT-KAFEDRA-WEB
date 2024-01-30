const topLink = document.querySelector(".top-link");
let imgs_carusel = document.querySelector(".mySwiper");
window.addEventListener("scroll", function () {
  const scrollHeight = window.pageYOffset;
  if (scrollHeight > 500) {
    topLink.classList.add("show-link");
  } else {
    topLink.classList.remove("show-link");
  }
});


const language = document.querySelectorAll(".btn_language");
language.forEach((element) => {
  element.addEventListener("click", () => {
    language.forEach((removeEleClass) => {
      removeEleClass.classList.remove("language_active");
    });
    element.classList.add("language_active");
  });
});

document.querySelectorAll(".jsImg").forEach((image) => {
  // console.log(image);
  image.addEventListener("click", (e) => {
    portfolioImgAjax(e.target.dataset.img_id);
    document.querySelector(".popup").style.display = "block";
    document.querySelector("body").style.overflowY = "hidden";
  });
});
document.querySelector(".popup span").addEventListener("click", () => {
  document.querySelector(".popup").style.display = "none";
  document.querySelector("body").style.overflowY = "scroll";
  imgs_carusel.innerHTML = "";
});
window.onclick = function(event) {
  if (event.target == document.querySelector(".popup")) {
    document.querySelector(".popup").style.display = "none";
    document.querySelector("body").style.overflowY = "scroll";
    imgs_carusel.innerHTML = "";
  }
}

function makeImgBlocks(data) {
  data.forEach(function (person) {
    showUsers(person);
  });
  function showUsers(imgs_data) {
    // console.log(imgs_data);
    const userDiv = document.createElement("div");
    userDiv.classList.add("item");
    userDiv.innerHTML = `<img class="w-100" src="${"/media/" + imgs_data.fields.img}" alt="" />`;
    imgs_carusel.appendChild(userDiv);
  }
}
// $(".owl-carousel").owlCarousel({
//   loop: true,
//   margin: 30,
//   autoplayHoverPause: true,
//   speed: 1,
//   responsiveClass: true,
//   URLhashListener: true,
//   startPosition: "URLHash",
//   center: true,
//   items: 1,
// });


