$(function(){
	// show college select form when clicked
	$('.show-college').on('click', function () {
		$('.display-college').fadeOut(250, function () {
			$('#college_select').fadeIn(500);
			$('#college_select').removeClass("hidden");
		});
	});
	// populate college dropdown when we guess wrong (never!)
	$('.dropdown-menu li').click(function(event) {
		var $target = $(event.currentTarget);
		var $drop = $('button.dropdown-toggle');

		$drop.text($target.text());
		school_domain = $('.dropdown-menu li').attr('value');
		$('.form-signin input[name=school]').attr('value', school_domain);
	});

	if($('input[name=school]').val()===""){
		$('.display-college').hide();
		$('#college_select').show();
		$("#joinCollege").attr("disabled", "disabled");
	}
	//choose college from list if not done magically
	$(".dropdown-menu li").click(function(){
		$('input[name=school]').val($(this).attr('value'));
		$("#joinCollege").removeAttr("disabled");  
    });
});
