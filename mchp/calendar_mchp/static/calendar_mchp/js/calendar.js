/*
 * calendar.js
 *
 * This file handles the functionality of the calendar page.
 */
$(document).ready(function() {
	// show calendar step three  when clicked
    $('.stepOneNext').on('click', function () {
    	$('#calStepOne').fadeOut(250, function () {
    		$('#calStepTwo').fadeIn(500);
    		$('#calStepTwo').removeClass("hidden");
    	});
	});
	// show calendar step three when clicked
    $('.stepTwoNext').on('click', function () {
	$('#calStepTwo').fadeOut(250, function () {
		$('#calStepThree').fadeIn(500);
		$('#calStepThree').removeClass("hidden");
		});
	});
	// switch to your cal list tab when clicked
	$('.stepThreeNext1').on('click', function () {
		$('.cal-intro').fadeOut(250, function () {
		$('#yourCalList').fadeIn(500);
		$('#yourCalList').removeClass("hidden");
		});
	});
	// switch to calendar list tab when clicked
	$('.stepThreeNext2').on('click', function () {
		$('.nav-tabs > .active').next('li').find('a').trigger('click');
		$('#col_1').addClass('col-md-8', 1000, "easeOutQuart");
		$('#col_2').addClass('col-md-4', 1000, "easeOutQuart");
	});
	// expand col_1 when cal list tab is clicked
	$('#calListTab').on('click', function () {
		$('#col_1').toggleClass('col-md-8', 1000, "easeOutQuart");
		$('#col_2').toggleClass('col-md-4', 1000, "easeOutQuart");
	});
	// contract col_1 when your cal tab is clicked
	$('#yourCalTab').on('click', function () {
		$('#col_1').removeClass('col-md-8', 1000, "easeOutQuart");
		$('#col_2').removeClass('col-md-4', 1000, "easeOutQuart");
	});
});
