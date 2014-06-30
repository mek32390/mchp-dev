$(function(){
	$('.dropdown-menu li').click(function(event) {
		var $target = $(event.currentTarget);
		var $drop = $('button.dropdown-toggle');

		$drop.text($target.text());
		school_domain = $('.dropdown-menu li').attr('value');
		$('.form-signin input[name=school]').attr('value', school_domain);
	});
});
