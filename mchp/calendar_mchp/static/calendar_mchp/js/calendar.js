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
		$('#col_1').addClass('col-sm-9', 1000, "easeOutQuart");
		$('#col_2').addClass('col-sm-3', 1000, "easeOutQuart");
		// $('.cal-intro').fadeOut(250);

	});
	// expand col_1 when cal list tab is clicked
	$('#calListTab').on('click', function () {
		$('#col_1').addClass('col-sm-9', 1000, "easeOutQuart");
		$('#col_1').removeClass('col-sm-3', 1000, "easeOutQuart");
		$('#col_2').addClass('col-sm-3', 1000, "easeOutQuart");
		$('#col_2').removeClass('col-sm-9', 1000, "easeOutQuart");
		$('#calendar').fullCalendar( 'changeView', 'agendaDay' );
	});
	// contract col_1 when your cal tab is clicked
	$('#yourCalTab').on('click', function () {
		$('#col_1').addClass('col-sm-3', 1000, "easeOutQuart");
		$('#col_2').switchClass('col-sm-3','col-sm-9', 1000, "easeOutQuart");
		$('#calendar').fullCalendar( 'changeView', 'month' );
	});
	
	// using jquery.cookie plugin
	var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	// csrf token stuff
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	/**********************
	 * FULLCALENDAR STUFF *
	 **********************/

	var today = new Date().toJSON().slice(0,10);
	var extract_event = function(event, dateDelta, minuteDelta) {
		event_data = {
			id: event.id,
			title: event.title,
			start: event.start._d.toJSON(),
			end: event.end._d.toJSON(),
			all_day: event.allDay,
		};
		save_event(event_data, false);
	};

	$('#calendar').fullCalendar({
		header: false,
    	weekMode: 'liquid',

		//trigger add event pop-up on click and stay
		dayClick: function(date, jsEvent, view) {
			$(this).popover('show');

		},
		
		events: {
			url: '/calendar/feed/',
			type: 'GET',
			success: function(data) {
			},
			error: function() {
				addMessage('Error getting events', 'danger');
			},
			// color: 'blue',   // a non-ajax option
			// textColor: 'black' // a non-ajax option
		},
		eventDrop: extract_event,
		eventResize: extract_event,

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
				save_event({title: title, start: start._d.toJSON(), end: end._d.toJSON()}, true); // create = true
			}
			$('#calendar').fullCalendar('unselect');
		},
		editable: true,
	});


	//	custom date above calendar, should be called each time a different view is triggered  
	$('.cal-date').html(function () {
		var view = $('#calendar').fullCalendar('getView');
		return view.title;
	});

	// CUSTOM HEADER BUTTONS FOR CAL

	// today button
	$('.cal-today-button').click(function() {
    	$('#calendar').fullCalendar('today');
	});
	// prev button
	$('.cal-prev-button').click(function() {
    	$('#calendar').fullCalendar('prev');
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});
	// next button
	$('.cal-next-button').click(function() {
    	$('#calendar').fullCalendar('next');
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});
	// month view button
	$('.cal-month-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'month' );
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});
	// agenda week view button
	$('.cal-agendaWeek-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'agendaWeek' );
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});
	// agenda day view button
	$('.cal-agendaDay-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'agendaDay' );
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});

});

var save_event = function (eventData, create) {
	console.log(eventData);
	var url = '';
	if (create) {
		url = '/calendar/events/add/';
	} else {
		url = '/calendar/events/update/';
	}
	$.ajax({
		url: url,
		type: 'POST',
		data: eventData,
		success: function(data) {
			console.log(data);
			$.each(data.messages, function(index, message){
				console.log(message);
				addMessage(message.message, message.extra_tags);
			});
		},
		fail: function(data) {
			addMessage('Failed to save event', 'danger');
		},
		always: function(data) {
		},
	});
};

