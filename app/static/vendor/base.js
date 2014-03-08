$(document).ready(function(){
	
	$('.tes1').mouseover(function(e){
		$('.tes2').parent().removeClass('open');
		$('.tes1').parent().addClass('open');
		});

	$('.tes2').mouseover(function(e){
		$('.tes1').parent().removeClass('open');
		$('.tes2').parent().addClass('open');
		});

	$('.cm').mouseover(function(e){
		$('.tes1').parent().removeClass('open');
		$('.tes2').parent().removeClass('open');
		});

	$('.hm').mouseover(function(e){
		$('.tes1').parent().removeClass('open');
		$('.tes2').parent().removeClass('open');
		});
	$('.hm').click(function(e){
		e.preventDefault();
		$(location).attr('href', '/');
		})
	$('.cm').click(function(e){
		e.preventDefault();
		$(location).attr('href', '/contact')
		})

});
