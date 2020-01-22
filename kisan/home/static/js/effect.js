/* start loader coding */
window.onload = function()

{
	"use strict";
	$(document).ready(function()
{
		$(".icon").fadeOut(1000,function(){
		$(".slide-left").animate({width:'0%'},500);
		$(".slide-right").animate({width:'0%'},500,function(){
		$(".loader-con").fadeOut();
		});
	});
});
	
};

	$(function(){
		"use strict";
		$("#menu").slicknav({
			label : '',
			brand : 'kisan-o-kiran',
		});
	});
/* end loader coding */

/* start big slider*/
$(document).ready(function() {
	"use strict";
  $(".skitter-large").skitter({
	  label : false,
	  dots : false,
	  
  });
});


$(document).ready(function(){
	$(".picone-header").slideDown(1000,function(){
		$(".picone-btn").fadeIn(1500,function(){
			$(".picone-header,.picone-btn").delay(50).fadeOut(function(){
				$(".slider-label").css({'background':'rgba(0,0,0,0.8)'});
				$(function(){
					$(".pictwo-header").fadeIn(1000,function(){
						$(".pictwo-para").show(1500,function(){
							$(".pictwo-btn").fadeIn(1000,function(){
								$(".pictwo-header,.pictwo-para,.pictwo-btn").delay(2800).fadeOut(function(){
									if($(window).width()>992)
									{$(".slider-label").css({'background':'inherit'})};
								});
							});
						});

											});
				})
			});
		});
	});
});





$(document).ready(

function(){setInterval(
	function(){
	$(".picone-header").slideDown(1000,function(){
		$(".picone-btn").fadeIn(1500,function(){
			$(".picone-header,.picone-btn").delay(50).fadeOut(function(){
				$(".slider-label").css({'background':'rgba(0,0,0,0.8)'});
				$(function(){
					$(".pictwo-header").fadeIn(1000,function(){
						$(".pictwo-para").show(1500,function(){
							$(".pictwo-btn").fadeIn(1000,function(){
								$(".pictwo-header,.pictwo-para,.pictwo-btn").delay(2800).fadeOut(function(){
									if($(window).width()>320){
									$(".slider-label").css({'background':'inherit'});}
								});
							});
						});

											});
				});
			});
		});
	});
},10500
);
}
);



/* end big slider*/


/* start project slider*/

$(document).ready(function(){
	"use strict";
	$(".center").slick({
		dots:false,
		infinite:true,
		centerMode:true,
		slidesToShow:3,
		slidesToScroll:3,
		responsive:[
			{
				breakpoint:768,
				settings:{
						dots:false,
						infinite:true,
						centerMode:true,
						slidesToShow:2,
						slideToScroll:3,
						centerPadding:'40px',
				}
			},
			
			{
				breakpoint:480,
				settings:{
					arrows:false,
					dots:false,
					infinite:true,
					slidesToShow:1,
					slidesToScroll:1,
					centerPadding:'20px',
				}
			},
			
		]
});

});

/* end project slider*/

/* start progressbar*/



/* end progressbar*/

/* start page scroll effect */

$(document).ready(function(){
	if($(window).width()>1024)
	{$(document).scroll(function(){
		var sheight = window.pageYOffset;
		if(sheight>950)
		{
			$(".my-pic,.about-text").slideDown(1000);

		}

		else{
			$(".my-pic,.about-text").slideUp(1000);
		}

		if(sheight>1233)
		{
			$(document).ready(function(){
	var pone = $('.progress-one').html();
	var ptwo = $('.progress-two').html();
	var pthree = $('.progress-three').html();
	var pfour = $('.progress-four').html();
	var pfive = $('.progress-five').html();
	$(".progress-one").animate({'width':pone},1000,function(){
		$('.progress-two').animate({'width':ptwo},500,function(){
			$('.progress-three').animate({'width':pthree},500,function(){
				$('.progress-four').animate({'width':pfour},500,function(){
					$('.progress-five').animate({'width':pfive},500);
				});
			});
		});
	});
});
		}

	});
}});

$(document).ready(function(){
	if($(window).width()>800 && $(window).width()<1024)
	{$(document).scroll(function(){
		var sheight = window.pageYOffset;
		if(sheight>520)
		{
			$(".my-pic,.about-text").slideDown(1000);

		}

		else{
			$(".my-pic,.about-text").slideUp(1000);
		}

		if(sheight>1120)
		{
			$(document).ready(function(){
	var pone = $('.progress-one').html();
	var ptwo = $('.progress-two').html();
	var pthree = $('.progress-three').html();
	var pfour = $('.progress-four').html();
	var pfive = $('.progress-five').html();
	$(".progress-one").animate({'width':pone},1000,function(){
		$('.progress-two').animate({'width':ptwo},500,function(){
			$('.progress-three').animate({'width':pthree},500,function(){
				$('.progress-four').animate({'width':pfour},500,function(){
					$('.progress-five').animate({'width':pfive},500);
				});
			});
		});
	});
});
		}

	});
}});
$(document).ready(function(){
	if($(window).width()<480)
	{$(document).scroll(function(){
		var sheight = window.pageYOffset;
		if(sheight>90)
		{
			$(".my-pic,.about-text").slideDown(1000);

		}

		else{
			$(".my-pic,.about-text").slideUp(1000);
		}

		if(sheight>1860)
		{
			$(document).ready(function(){
	var pone = $('.progress-one').html();
	var ptwo = $('.progress-two').html();
	var pthree = $('.progress-three').html();
	var pfour = $('.progress-four').html();
	var pfive = $('.progress-five').html();
	$(".progress-one").animate({'width':pone},1000,function(){
		$('.progress-two').animate({'width':ptwo},500,function(){
			$('.progress-three').animate({'width':pthree},500,function(){
				$('.progress-four').animate({'width':pfour},500,function(){
					$('.progress-five').animate({'width':pfive},500);
				});
			});
		});
	});
});
		}

	});
}});

$(document).ready(function(){
	if($(window).width()>480 && $(window).width()<800)
	{$(document).scroll(function(){
		var sheight = window.pageYOffset;
		if(sheight>460)
		{
			$(".my-pic,.about-text").slideDown(1000);

		}

		else{
			$(".my-pic,.about-text").slideUp(1000);
		}

		if(sheight>900)
		{
			$(document).ready(function(){
	var pone = $('.progress-one').html();
	var ptwo = $('.progress-two').html();
	var pthree = $('.progress-three').html();
	var pfour = $('.progress-four').html();
	var pfive = $('.progress-five').html();
	$(".progress-one").animate({'width':pone},1000,function(){
		$('.progress-two').animate({'width':ptwo},500,function(){
			$('.progress-three').animate({'width':pthree},500,function(){
				$('.progress-four').animate({'width':pfour},500,function(){
					$('.progress-five').animate({'width':pfive},500);
				});
			});
		});
	});
});
		}

	});
}});
$(document).ready(function(){
	var sh = window.pageYOffset;
	$(".check").html()
});
/* end page scroll effect*/
$(document).ready(function(){
	$(document).scroll(function(){
	var sh = window.pageYOffset;
	$(".check").html(sh);
});
	});
document.onkeydown=function(event){
		if(event.ctrlKey && event.keyCode==85)
		{
			return false;
		}
	}