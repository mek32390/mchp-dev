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
		    // when the meeting days button option changes
			$("input[name='course_days']:checkbox").click(function() {
			    if ($("input[id='mon']:checkbox").is(':checked')) {
		        	$('.course-time-mon').toggleClass('hidden');
		    	}
		    	else if ($("input[id='tue']:checkbox").is(':checked')) {
		        	$('.course-time-tue').fadeIn(500).removeClass('hidden');
		    	}
		    	else if ($("input[id='wed']:checkbox").is(':checked')) {
		        	$('.course-time-wed').fadeIn(500).removeClass('hidden');
		    	}
		    	else if ($("input[id='thur']:checkbox").is(':checked')) {
		        	$('.course-time-thur').fadeIn(500).removeClass('hidden');
		    	}
		    	else if ($("input[id='fri']:checkbox").is(':checked')) {
		        	$('.course-time-fri').fadeIn(500).removeClass('hidden');
		    	}

		    });
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


	/**********************
	 * FULLCALENDAR STUFF *
	 **********************/
	var dayDisplay = 'dddd';
	if($(window).width() < 620) {
		dayDisplay = 'ddd';
	}

	$('#calendar').fullCalendar({
		aspectRatio: 2,
		allDaySlot: false,
		columnFormat: {
			week: dayDisplay
		},
		defaultView: 'agendaWeek',
		editable: true,

		events: {
		},

		firstDay: 1,
		header: {
			left: '',
			center: 'title',
			right:'',
		},
		// minTime: "06:00:00",
		// maxTime: "23:00:00",
		// eventDrop: updateEvent,
		// eventResize: updateEvent,

		// defaultDate: today,
		selectable: true,
		selectHelper: true,
		select: function(start, end) {
			var title = prompt('Event Title:');
			var eventData;
			console.log(start);
			console.log(end._d.getTime());
			var calendar = $('#calendar').fullCalendar('getCalendar');
			var m = calendar.moment();
			console.log(m);
			var newEnd = new Date(end._d.getTime() + 45*60000);
			console.log(newEnd);
			end._d = newEnd;
			if (title) {
				eventData = {
					title: title,
					start: start,
					end: end
				};
				$('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
			}
		},
		snapDuration: "00:15:00"
	});
	$('.fc-center h2').text('Class Schedule');

});
