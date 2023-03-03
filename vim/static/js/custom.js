$(".menu-icon").click(function () {
  $(".menu-icon").toggleClass("open-menu");
  $(".menu-section").toggleClass("close-menu");
});
$(".menu-section li").click(function () {
  $(".menu-section").removeClass("close-menu");
  $(".menu-icon").removeClass("open-menu");
});

$(window).scroll(function () {
  if ($(this).scrollTop() > 300 && $(this).width() > 1008) {
    $(".header").addClass("fixed");
  } else {
    $(".header").removeClass("fixed");
  }
});

var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  loop:true,
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
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
  direction: "vertical",
  
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  
});



$(document).ready(function(){
  $(".section1").click(function(){
      $("#secoundBox").css("display", "none");
      $("#firstBox").css("display", "block");
     
  });
  
  $(".section2").click(function(){
      $("#firstBox").css("display", "none");
      $("#secoundBox").css("display", "block");
  });
});


