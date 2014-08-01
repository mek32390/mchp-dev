/*
 * calendar.js
 *
 * This file handles the functionality of the calendar page.
 */
$(document).ready(function() {
	if($('#calStepOne').length) {
		$('#yourCalList').hide();
	}
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
	// switch to your cal list when clicked and close intro
	$('.stepThreeNext').on('click', function () {
		$('.cal-intro').fadeOut(250, function () {
			$('#yourCalList').fadeIn(500);
		});
		toggle_flag();
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
	var updateEvent = function(event, dateDelta, minuteDelta) {
		eventData = {
			id: event.id,
			title: event.title,
			start: event.start._d.toJSON(),
			end: event.end._d.toJSON(),
			all_day: event.allDay,
		};
		saveEvent(eventData, false);
	};

	$('#calendar').fullCalendar({
		header: false,
    	weekMode: 'liquid',

		//trigger add event pop-up on click and stay
		dayClick: function(date, jsEvent, view) {
			// remove the other popovers
			$('.popover').remove();
			// show the clicked day popover
			$(jsEvent.target).popover('show');
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
		eventClick: function(calEvent, jsEvent, view) {
			eventData = {
				id: calEvent.id,
				title: calEvent.title,
				start: calEvent.start._d.toJSON(),
				end: calEvent.end._d.toJSON(),
				all_day: calEvent.allDay,
			};
			deleteEvent(eventData);
			$('#calendar').fullCalendar('removeEvents', calEvent.id);
			return false;
		},
		eventDrop: updateEvent,
		eventResize: updateEvent,

		// don't delete this yet
		// defaultDate: today,
			// 	eventData = {
			// 		title: title,
			// 		start: start,
			// 		end: end
			// 	};
			// 	$('#calendar').fullCalendar('renderEvent', 
			// 	eventData, true); // stick? = true
			// 	saveEvent({title: title, start: 
			// 	start._d.toJSON(), end: end._d.toJSON()}, true); // create = true
			// }
		editable: true,
	});

	/*****************
	 * popover stuff *
	 *****************/
	// initalize the popovers for individual cal days
	$('.fc-day').popover({
		trigger: 'manual',
		placement: 'auto left',
		html: true,
		viewport: '#calendar',
		title: function() {
			return $('#popover-title').html();
		},
		content: function() {
			return $('#popover-content').html();
		},
		container: 'body',
	});
	// close the popovers when you click outside
	// this is add to the body so it can be registered
	// with dynamically added popovers
	$('body').on('click', function (e) {
    	$('.fc-day').each(function () {
        //the 'is' for buttons that trigger popups
        //the 'has' for icons within a button that triggers a popup
	        if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
	            $(this).popover('hide');
	        }
    	});
    	//display selected calendar in create event popover upper right
    	$("#calSelect > li a").click(function(){
	        //display the selected calendar in the button
	        $(".cal-name").text($(this).text());
	        $(".cal-name").val($(this).text()).append(' ');
    	});
	});


	// $('body').on('click', 'fc-day', function() {
	// 	$('.popover').popover('hide');
	// });
	// $('body').on('click', '.close-popover', function() {
	// 	$('.popover').popover('toggle');
	// });
	// same, but with submitting the form in the popover
	$('body').on('submit', '#add-event-form', function(event) {
		return false;
	});

	/*********************************
	 * CUSTOM HEADER BUTTONS FOR CAL *
	 *********************************/
	//	custom date above calendar 
	$('.cal-date').html(function () {
		var view = $('#calendar').fullCalendar('getView');
		return view.title;
	});

	// today button
	$('.cal-today-button').click(function() {
    	$('#calendar').fullCalendar('today');
	});

	// prev button
	$('.cal-prev-button').click(function() {
    	$('#calendar').fullCalendar('prev');
	});
	// next button
	$('.cal-next-button').click(function() {
    	$('#calendar').fullCalendar('next');
	});
	// month view button
	$('.cal-month-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'month' );
	});
	// agenda week view button
	$('.cal-agendaWeek-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'agendaWeek' );
	});
	// agenda day view button
	$('.cal-agendaDay-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'agendaDay' );
	});

	// change the title when the view changes
	$('.cal-button').click(function() {
    	$('.cal-date').text(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});

});

var saveEvent = function (eventData, create) {
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
		complete: function(data) {
		},
	});
};

var deleteEvent = function(eventData) {
	$.ajax({
		url: '/calendar/events/delete/',
		type: 'POST',
		data: eventData,
		success: function(data) {
			$.each(data.messages, function(index, message){
				console.log(message);
				addMessage(message.message, message.extra_tags);
			});
		},
		fail: function(data) {
			addMessage('Failed to delete event', 'danger');
		},
		complete: function(data) {
		},
	});
};

var toggle_flag = function() {
	$.ajax({
		url: '/profile/toggle-flag/',
		type: 'POST',
		data: {'flag': 'calendar_tutorial'},
	});
};
