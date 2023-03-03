$(".menu-icon").click(function () {
  $(".menu-icon").toggleClass("open-menu");
  $(".menu-section").toggleClass("close-menu");
});
$(".menu-section li").click(function () {
  $(".menu-section").removeClass("close-menu");
  $(".menu-icon").removeClass("open-menu");
});

$(window).scroll(function () {
  if ($(this).scrollTop() > 00 && $(this).width() > 1008) {
    $(".header").addClass("fixed");
  } else {
    $(".header").removeClass("fixed");
  }
});





var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 30,
  loop:true,
  autoplay: true,
  speed: 1500,
 breakpoints: {
  280: {
    slidesPerView: 1,
  },
  576: {
    slidesPerView: 2,
  },
  1024: {
    slidesPerView: 3,
  },
},
});


var swiper = new Swiper(".mySwiper1", {
  loop:true,
  autoplay:true,
  pagination: {
    el: ".swiper-pagination",
  },
});

var swiper = new Swiper(".mySwiper2", {
  slidesPerView: 3,
  spaceBetween: 30,
  loop:true,
 autoplay:true,
 breakpoints: {
  280: {
    slidesPerView: 1,
  },
  576: {
    slidesPerView: 2,
  },
  1024: {
    slidesPerView: 3,
  },
},
});
