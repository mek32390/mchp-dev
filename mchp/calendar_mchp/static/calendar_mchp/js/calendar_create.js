/*
 * calendar_create.js
 *
 * This file handles the functionality of the calendar create page.
 */
$(function() {

	// When the calendar types's value changes
	$("input[name='calTypes']:radio").change(function() {

		// If the class calendar option is selected
		if ($('#classCal').is(':checked')) {
		    $('.course-fields').fadeIn(500).removeClass('hidden');
		    $('.cal-name').fadeOut(500);
		    $('.cal-submit').addClass('hidden');
		    // when the sell/not sell option changes
		    $("input[name='cal_sell']:radio").change(function() {
			    if ($('#sell').is(':checked')) {
		        	$('.cal-description').fadeIn(500).removeClass('hidden');
		        	$('.cal-submit').fadeIn(600).removeClass('hidden');
		    	}
		    	else {
		    		$('.cal-description').fadeOut(500);
		    		$('.cal-submit').fadeIn(600).removeClass('hidden');
		    		$('.cal-submit').fadeIn(600).removeClass('hidden');
		    	}
		   	});
		}

		// Else if the personal calendar option is selected
		else if ($('#personalCal').is(':checked')) {
		    $('.cal-name').fadeIn(500).removeClass('hidden');
		    $('.course-fields').fadeOut(500);
		    $('.cal-description').fadeOut(500);
		    $('.cal-submit').fadeIn(600).removeClass('hidden');
		}
	});

	// reset form on page reload or other unload actions
	$( window ).unload(function() {
		$('#calendar_create')[0].reset();
	});	

});




	
