window.addEventListener('DOMContentLoaded', () => {
  // $('.dropdown-toggle').dropdown()
   // ---------------- Навыки ---------------- //
   const skillbar = document.querySelectorAll(".skillbar")
   const triggerBottom = window.innerHeight / 5 * 4
   const box = document.querySelector("#section_skills")

   if(box != null) {
    window.addEventListener('scroll', checkBoxes)
    checkBoxes()
   }

   function checkBoxes() {
    const boxTop = box.getBoundingClientRect().top
    if(boxTop < triggerBottom) {
      window.removeEventListener('scroll', checkBoxes)
      skillbar.forEach(element => {
        const skillbarBar = element.querySelector(".skillbar-bar")
        const dataPercent = +element.getAttribute('data-percent')
        let counter = 0
        const updateCounter = () => {
          if(counter < dataPercent) {
            counter = counter + 0.5
            skillbarBar.style.width = counter + '%';
            setTimeout(updateCounter, 1)
          } else {
            skillbarBar.style.width = counter + '%';
          }
        }
        updateCounter()
      });
    }
   }

  //  ------------ Слайдер ------------ //
   $('.caruosel__inner').slick({
    //dots: true,
    speed: 1500,
    //adaptiveHeight: true,
    autoplay: true,
    autoplaySpeed: 1500,
    dots: true,
    //fade: true,
    //cssEase: 'linear'
    prevArrow: '<button type="button" class="slick-prev"><img src="/"></button>',
    nextArrow: '<button type="button" class="slick-next"><img src="/"></button>',
    responsive: [
        {
            breakpoint: 992,
            settings: {
                dots: true,
                arrows: false
            }
        }
    ]
  });
  $('ul.catalog__tabs').on('click', 'li:not(.catalog__tab_active)', function() {
    $(this)
      .addClass('catalog__tab_active').siblings().removeClass('catalog__tab_active')
      .closest('div.conteiner').find('div.catalog__content').removeClass('catalog__content_active').eq($(this).index()).addClass('catalog__content_active');
  });

    function toggleSlide(item) {
        $(item).each(function(i){
            $(this).on('click', function(e){
                e.preventDefault();
                $('.catalog-item__content').eq(i).toggleClass('catalog-item__content_active');
                $('.catalog-item__content_description').eq(i).toggleClass('catalog-item__content_description_active');
            })
        });
    };

    toggleSlide ('.catalog-item__link');
    toggleSlide ('.catalog-item__back');
});   