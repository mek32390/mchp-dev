$(function(){
	// show college select form when clicked
	$('.show-college').on('click', function () {
		$('.display-college').fadeOut(250, function () {
			$('#college_select').fadeIn(500);
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
});
