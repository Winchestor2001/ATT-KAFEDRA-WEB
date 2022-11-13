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
  image.addEventListener("click", () => {
    document.querySelector(".popup").style.display = "block";
    document.querySelector(".popup-image img").src = image.getAttribute("src");
  });
});
document.querySelector(".popup span").addEventListener("click", () => {
  document.querySelector(".popup").style.display = "none";
});
