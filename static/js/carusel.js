$(document).ready(function () {
    $('.carousel').owlCarousel({
        loop: true,
        // margin: 30,
        autoplay: true,
        animateOut: 'fadeOut',
        autoplayTimeout: 4000,
        // autoplayHoverPause: true,
        speed: 8000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            992: {
                items: 3
            }
        }
    })
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        animateOut: 'fadeOut',
        autoplayTimeout: 4000,
        // autoplayHoverPause: true,
        speed: 8000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            }
        }
    });


})
// Glassary Tooltips
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
const popover = new bootstrap.Popover('.popover-dismiss', {
    trigger: 'focus'
  })