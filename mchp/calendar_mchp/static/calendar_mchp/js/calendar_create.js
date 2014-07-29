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

		    // it would be better if the "sell radios" only were shown when an actual course option was selected
		    // this currently isn't being used because it doesnt work
		    $('.course-select option').each(function() {
		    	if(!$(this).is(':selected')) {
		    		$('.cal-sell').fadeIn(250).removeClass('hidden');
		    	}
		    });

    		// when the sell/not sell option changes
    		$("input[name='cal_sell']:radio").change(function() {
    			if ($('#sell').is(':checked')) {
    				$('.course-meetings').fadeIn(500).removeClass('hidden');
    				$('.cal-start-end').fadeIn(500).removeClass('hidden');
    				$('.cal-description').fadeIn(500).removeClass('hidden');

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
   	$("#mon").on('click', function() {
   		$(".mon-times").fadeIn(250).toggleClass('hidden');
   	});
   	$("#tues").on('click', function() {
   		$(".tues-times").fadeIn(250).toggleClass('hidden');
   	});
   	$("#wed").on('click', function() {
   		$(".wed-times").fadeIn(250).toggleClass('hidden');
   	});
   	$("#thur").on('click', function() {
   		$(".thur-times").fadeIn(250).toggleClass('hidden');
   	});
   	$("#fri").on('click', function() {
   		$(".fri-times").fadeIn(250).toggleClass('hidden');
   	});
   	$("#sat").on('click', function() {
   		$(".sat-times").fadeIn(250).toggleClass('hidden');
   	});
   	$("#sun").on('click', function() {
   		$(".sun-times").fadeIn(250).toggleClass('hidden');
   	});

	// initialize date picker
	$('.input-group.date').datepicker({
		startView: 1,
		multidate: false,
		autoclose: true,
		todayHighlight: true
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

