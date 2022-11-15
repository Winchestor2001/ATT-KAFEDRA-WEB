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
  image.addEventListener("click", (e) => {
    console.log("success");
    document.querySelector(".popup").style.display = "block";
    let pdf_div = document.querySelector(".canvas");
    // pdf_div.dataset.pdf = e.target.dataset.pdf
    pdf_div.innerHTML = `
          <canvas data-pdf="${e.target.dataset.pdf}" class="w-75 h-100 jsImg shadow pdf_render">
          </canvas>
    `;
    renderPDFFiles();
  });
});
document.querySelector(".popup span").addEventListener("click", () => {
  document.querySelector(".popup").style.display = "none";
});
