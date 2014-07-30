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
				$('.course-meetings').fadeIn(500).removeClass('hidden');
				$('.cal-start-end').fadeIn(500).removeClass('hidden');
				$('.cal-description').fadeIn(500).removeClass('hidden');
				$('.cal-submit').fadeIn(600).removeClass('hidden');
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
		$('#calendar-create')[0].reset();
	});	

	// bootstrap validator
	$('#calendar-create').bootstrapValidator({
        fields: {
        	course: {
                validators: {
                    notEmpty: {
                        message: 'Please choose a class'
                    }
                }
            },
            private: {
                validators: {
                    notEmpty: {
                        message: 'Please select one of the options above'
                    }
                }
            },
            clockstart: {
            	trigger: 'blur',
                validators: {
                    notEmpty: {
                        message: 'Your class start time is required'
                    }
                }
            },
            clockend: {
            	trigger: 'blur',
                validators: {
                    notEmpty: {
                        message: 'Your class end time is required'
                    }
                }
            },
            enddate: {
                validators: {
                    notEmpty: {
                        message: 'Your class end date is required'
                    }
                }
            },
            description: {
                validators: {
                    notEmpty: {
                        message: 'Don\'t you want your classmates to buy this?'
                    }
                }
            },
        }
	})
	.on('success.form.bv', function(e) {
		// Prevent form submission
		e.preventDefault();
	});

	/***********************
	 * Submitting the form *
	 ***********************/
	$('#calendar-create').submit(function(event){
		// all the days the user selected
		var $days = $('.day-button.active');
		var times = {};
		var error = false;
		$days.each(function(index, day){
			// get the times from the user
			day_name = $(day).data('day');
			var $start = $("#" + day_name + "-clock-start");
			var $end = $("#" + day_name + "-clock-end");
			if($start.val() ==='' || $end.val()=== '') {
				addMessage('A day must have both a start and end date', 'info');
				error = true;
			}
			// parse them
			var start_moment = moment($start.val(), "hh:mmA");
			var end_moment = moment($end.val(), "hh:mmA");
			// validate them
			if(start_moment > end_moment) {
				error = true;
				addMessage('Start times must come before end times', 'info');
			}
			// add them to the json object
			times[day_name] = {
				'start': start_moment,
				'end': end_moment,
			};
		});
		// add object to the form
		var data = $(this).serialize();
		times = JSON.stringify(times);
		data += "&times=" + encodeURIComponent(times);

		// submit the form if it was valid
		if (!error) {
			$.ajax({
				method: 'post',
				url: '/calendar/create/',
				data: data,
				success: function(data) {
					window.location.href = "/calendar/";
				},
				complete: function(data) {
					if (data.hasOwnProperty('responseJSON') && data.responseJSON.hasOwnProperty('messages')) {
						$.each(data.responseJSON.messages, function(index, message) {
							console.log(message);
							addMessage(message.message, message.extra_tags);
						});
					}
				}
			});
		}
		return false;
	});
});
