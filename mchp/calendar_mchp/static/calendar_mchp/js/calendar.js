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
		$('#col_1').addClass('col-sm-8', 1000, "easeOutQuart");
		$('#col_2').addClass('col-sm-4', 1000, "easeOutQuart");
		// $('.cal-intro').fadeOut(250);

	});
	// expand col_1 when cal list tab is clicked
	$('#calListTab').on('click', function () {
		$('#col_1').addClass('col-sm-8', 1000, "easeOutQuart");
		$('#col_1').removeClass('col-sm-4', 1000, "easeOutQuart");
		$('#col_2').addClass('col-sm-4', 1000, "easeOutQuart");
		$('#col_2').removeClass('col-sm-8', 1000, "easeOutQuart");
	});
	// contract col_1 when your cal tab is clicked
	$('#yourCalTab').on('click', function () {
		$('#col_1').addClass('col-sm-4', 1000, "easeOutQuart");
		$('#col_2').switchClass('col-sm-4','col-sm-8', 1000, "easeOutQuart");
	});
	
	/**********************
	 * FULLCALENDAR STUFF *
	 **********************/

	var today = new Date().toJSON().slice(0,10);

	$('#calendar').fullCalendar({
		// put your options and callbacks here
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek,agendaDay'
		},
		events: {
			url: '/calendar/feed/',
			type: 'GET',
			error: function() {
				addMessage('Error getting events', 'danger');
			},
			// color: 'blue',   // a non-ajax option
			// textColor: 'black' // a non-ajax option
		},
		// defaultDate: today,
		selectable: true,
		selectHelper: true,
		select: function(start, end) {
			var title = prompt('Event Title:');
			var eventData;
			if (title) {
				eventData = {
					title: title,
					start: start,
					end: end
				};
				$('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
			}
			$('#calendar').fullCalendar('unselect');
		},
		editable: true,
	});

});
