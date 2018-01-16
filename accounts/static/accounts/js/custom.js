
// preloader
$(window).load(function(){
    $('.preloader').fadeOut(500); // set duration in brackets    
});

$(document).ready(function() {

	
    
    /* history*/
    $(".buttonsing").click(function(){
               $(".form").toggle(1000);
                $(".buttonsing").css("display","none");
            });
   
    $(".forget").click(function(){
       $(".formpassword").toggle(1000);
       $(".formOn").fadeOut('slow');
       $(".forBack").fadeIn(1000);
    });
    $(".forBack").click(function(){
       $(".formpassword").fadeOut(1000);
       $(".formOn").fadeIn('slow');
       $(".forBack").fadeOut('slow');
    });
	/* Hide mobile menu after clicking on a link
    -----------------------------------------------*/
    $('dropdown-toggle').click(function(){
        $('dropdown-menu').toggle();
    });
    $('html').click(function(){
        $(".navbar-collapse").collapse('hide');
    });
    
	
		    
    // jQuery to collapse the navbar on scroll //
	$(window).scroll(function() {
	    if ($(".navbar").offset().top > 50) {
	        $(".navbar-fixed-top").addClass("top-nav-collapse");
            $(".dropdown-menu").css("background-color","#6ae9d0");
	    } else {
	        $(".navbar-fixed-top").removeClass("top-nav-collapse");
            $(".dropdown-menu").css("background-color","transparent");
	    }
	});
	
   
	

	/* wow
	-------------------------------*/
	new WOW().init();
});
