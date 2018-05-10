$( document ).ready(function() {

  /*--- scroll page ---*/
  $('.scrollink[href^="#"]').on('click', function(event) {
      var target = $(this.getAttribute('href'));
      if( target.length ) {
          event.preventDefault();
          $('html, body').stop().animate({
              scrollTop: target.offset().top - 100
          }, 600);
      }
  });

  /*-- tabs --*/
  $('.tabs a').click(function(event){
    event.preventDefault();
    var tablink = $(this).attr('id');

    if($(this).hasClass('inactive')){
      $('.tabs a').addClass('inactive');
      $(this).removeClass('inactive');

      $('.content-tab').hide();
      $('#'+ tablink + 'C').fadeIn('slow');
   }
  });

});