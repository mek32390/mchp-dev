/*
 * calendar_create.js
 *
 * This file handles the functionality of the calendar create page.
 */
$(function() {

	// When the calendar types's value changes
	$("input[name='cal-type']:radio").change(function() {

		// If the class calendar option is selected
		if ($('#classCal').is(':checked')) {
			$('.course-fields').fadeIn(500).removeClass('hidden');
			$('.cal-name').fadeOut(500);
			$('.cal-submit').addClass('hidden');

		    // it would be better if the "sell radios" only were shown when an actual course option was selected
		    // this currently isn't being used because it doesnt work
		    $('.course-select option').each(function() {
		    	if(!$(this).is(':selected')) {
		    		$('.cal-sell').fadeIn(250).removeClass('hidden');
		    	}
		    });

    		// when the sell/not sell option changes
    		$("input[name='private']:radio").change(function() {
    			if ($('#sell').is(':checked')) {
    				$('.course-meetings').fadeIn(500).removeClass('hidden');
    				$('.cal-start-end').fadeIn(500).removeClass('hidden');
    				$('.cal-description').fadeIn(500).removeClass('hidden');
    				$('.cal-submit').fadeIn(600).removeClass('hidden');
    			}
    			else {
    				$('.course-meetings').fadeOut(500);
    				$('.cal-start-end').fadeOut(500);
    				$('.cal-description').fadeOut(500);
    				$('.cal-submit').fadeIn(600).removeClass('hidden');
    			}
    		});
    	}
		// Else if the personal calendar option is selected
		else if ($('#personalCal').is(':checked')) {
			$('.cal-name').fadeIn(500).removeClass('hidden');
			$('.course-fields').fadeOut(500);
			$('.cal-submit').fadeIn(600).removeClass('hidden');
		}
	});

	// initializing clockpicker
	$('.clockpicker').clockpicker( {
		twelvehour: 'true'
	});

   	// when the meeting days button option changes
   	$(".day-button").click(function(event) {
		$(event.target).siblings('.day-times').fadeIn(250).toggleClass('hidden');
   	});

	// initialize date picker
	$('.input-group.date').datepicker({
		startView: 1,
		multidate: false,
		autoclose: true,
		todayHighlight: false
	});

	// reset form on page reload or other unload actions
	$( window ).unload(function() {
		$('#calendar_create')[0].reset();
	});	
});
