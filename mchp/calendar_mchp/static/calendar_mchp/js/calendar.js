/*
 * calendar.js
 *
 * This file handles the functionality of the calendar page.
 */
$(function() {

	/*******************************
	 * FOR EDITING CALENDAR EVENTS *
	 *******************************/
	$.fn.editable.defaults.error = function(data) {
		$('.editable-errors').text(data.responseJSON.response);
	};
	$.fn.editable.defaults.success = function(data) {
		$('.editable-success').text(data.response);
	};

	// The following editables are still a work in progress
	// make title editable
	var eventEditUrl = '/calendar/events/update/';
	$('.edit-event-title').editable({
	    	mode: 'inline',
	    	inputclass: '',
			url: eventEditUrl,
			unsavedclass: 'text-danger',
			emptyclass: '',
			emptytext: 'Enter an Event Title',
			highlight: '',
			onblur: 'submit',				
			send: 'always',
	});
	// initialize date picker
	// this is duplicated code from below but I needed it to work
	$('input.date').datepicker({
		format: "D M d, yyyy", //"yyyy-m-d"
	    startDate: "today",
		autoclose: true,
		todayHighlight: true
    }).on('changeDate', function(event) {
		var pick = moment(event.date);
		$('.date-input').data('date', pick);
	});
    // make date editable
    // this is needed because the datepicker wont fire unless an input is visible
	$('.date-holder').on('click', function() {
		$('.date-input').removeClass('hidden');
		$('.date-holder').addClass('hidden');
	});
	// return to standard editable format after datepicker closes
	$('.date-input').datepicker()
    .on('hide', function(){
        $('.date-input').addClass('hidden');
		$('.date-holder').removeClass('hidden');
    });

    // initializing clockpicker
	$('.clockpicker').clockpicker( {
		twelvehour: 'true',
		// afterHide: function() {
  //                           alert(yes);
  //                       }
		// placement: 'top',
    	// align: 'left',
	});
    // make time editable
    // this is needed because the clockpicker wont fire unless an input is visible
	$('.time-holder').on('click', function() {
		$('.time-input').removeClass('hidden');
		$('.time-holder').addClass('hidden');
	});
	// return to standard editable format after datepicker closes
	// $('.time-input').clockpicker()
 //    .on('hide', function(){
 //        $('.time-input').addClass('hidden');
	// 	$('.time-holder').removeClass('hidden');
 //    });


    // make the event time editable
	// $('.edit-event-time').editable({
	//     	mode: 'inline',
	//     	inputclass: '',
	// 		url: '',
	// 		unsavedclass: 'text-danger',
	// 		emptyclass: '',
	// 		emptytext: 'Enter an Event Title',
	// 		highlight: '',
	// 		onblur: 'submit',				
	// 		send: 'always',
	// 		value: 1,
	// 		source: [
	// 			{value: 1, text: 'in Class'},
	// 			{value: 2, text: 'by Midnight'},
	// 			{value: 3, text: 'Other...'}
	// 		]
	// });
	// make the class editable
	$('.edit-event-class').editable({
	    	mode: 'inline',
	    	inputclass: '',
			url: '',
			unsavedclass: 'text-danger',
			emptyclass: '',
			highlight: '',
			onblur: 'submit',				
			send: 'always',
			value: 1,
			source: [
				{value: 1, text: 'ECON 200'},
				{value: 2, text: 'ACCT 200'},
				{value: 3, text: 'MKTG 361'}
			]
	});
	// replacing the description with notes
	$('.edit-event-description').editable({
	    	mode: 'inline',
	    	inputclass: '',
			url: eventEditUrl,
			unsavedclass: 'text-danger',
			emptyclass: '',
			emptytext: 'description',
			highlight: '',
			onblur: 'submit',				
			send: 'always',
			rows: 3,
	});


	/**************************
	 * FOR MANAGING CALENDARS *
	 **************************/

	var calendarEditUrl = '/calendar/update/';
	// make the class editable
	$('.calendar-selling').editable({
	    	mode: 'inline',
	    	inputclass: '',
			url: '',
			unsavedclass: 'text-danger',
			emptyclass: '',
			highlight: '',
			onblur: 'submit',				
			send: 'always',
			value: 1,
			source: [
				{value: 1, text: 'Yes'},
				{value: 2, text: 'No'},
			]
	});

	 // make calendar price editable
	$('.calendar-price').editable({
	    	mode: 'inline',
	    	inputclass: '',
			url: '',
			unsavedclass: 'text-danger',
			emptyclass: '',
			emptytext: 'Enter a price for this calendar',
			highlight: '',
			onblur: 'submit',				
			send: 'always',
	});

	// for the calendar description
	$('.calendar-description').editable({
	    	mode: 'inline',
	    	inputclass: '',
			url: '',
			unsavedclass: 'text-danger',
			emptyclass: '',
			emptytext: '',
			highlight: '',
			onblur: 'submit',				
			send: 'always',
	});

	// when the modal pops up, fill in the right info
	// this modal gets it events when a event hover popover is created
	// and it gets the pk from the link that was clicked to open it
	$('#event-edit-modal').on('shown.bs.modal', function() {
		var $modal = $('#event-edit-modal');
		var events = $modal.data('events');
		var pk = $modal.data('event-id');
		var event = null;
		$.each(events, function(index, e) {
			if(e.id == pk) {
				event = e;
			}
		});
		// give the modal the event specific information
		date_string = 'ddd MMM DD, YYYY';
		$modal.find('.edit-event-title').editable('option', 'value', event.title);
		$modal.find('.edit-event-title').editable('option', 'pk', event.id);
		$modal.find('.edit-event-title').editable('option', 'name', 'title');

		$modal.find('.edit-event-date').editable('option', 'value', event.start.format(date_string));
		$modal.find('.edit-event-date').editable('option', 'pk', event.id);
		$modal.find('.edit-event-date').editable('option', 'name', 'date');

		$modal.find('.edit-event-time').editable('option', 'value', event.start.format('hh:mm a'));
		$modal.find('.edit-event-time').editable('option', 'pk', event.id);
		$modal.find('.edit-event-time').editable('option', 'name', 'time');

		$modal.find('.edit-event-class').editable('option', 'value', event.course);
		$modal.find('.edit-event-class').editable('option', 'pk', event.id);
		$modal.find('.edit-event-class').editable('option', 'name', 'class');

		$modal.find('.edit-event-description').editable('option', 'value', event.description);
		$modal.find('.edit-event-description').editable('option', 'pk', event.id);
		$modal.find('.edit-event-description').editable('option', 'name', 'description');
	});

	/*******************************
	 * CALENDAR INTRODUCTION STUFF *
	 *******************************/

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
		toggle_flag('calendar_tutorial');
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

	$('.confirm-delete-button').click(function() {
		var pk = $(this).data('cal');
		deleteCalendar(pk);
		// remove from cal list
		var $link_parent = $('#owned-calendar-holder-'+pk);
		$link_parent.fadeOut(500, function() {
			$link_parent.remove();
			var count = parseInt($('#owned-calendar-count').text()) - 1;
			$('#owned-calendar-count').text(count);
			if (count < 1) {
				$('#make-a-calendar').removeClass('hidden');
			}
		});
		// remove from manage modal
		var modal = $('#manage-calendars');
		modal.find('#edit-calendar-link-'+pk).remove();
		modal.find('#edit-calendar-tab-'+pk).remove();
	});

	$('.pre-delete-button').click(function() {
		var $modal = $('#delete-cal-modal');
		var pk = $(this).data('cal');
		$('.confirm-delete-button').data('cal', pk);
		$modal.modal('show');
	});

	/**********************
	 * FULLCALENDAR STUFF *
	 **********************/

	var today = new Date().toJSON().slice(0,10);
	var updateEvent = function(event, dateDelta, minuteDelta) {
		eventData = {
			id: event.id,
			title: event.title,
			start: event.start.toJSON(),
			end: event.end.toJSON(),
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
			date_string = date.format('ddd MMM DD, YYYY');
			$('.date-input').data('date', date);
			$('.date-input').attr('value', date_string);

			$(this).popover({
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
			$(this).popover('show');
		},

		events: {
			url: '/calendar/feed/',
			type: 'GET',
			success: function(data) {
				var events = [];
				$.each(data.events, function(index, event) {
					events.push({
						'start': moment.utc(event.start),
						'end': moment.utc(event.end),
						'id': event.id,
						'title': event.title,
						'description': event.description,
						'course': event.course,
						'color': event.calendar__color,
					});
					console.log(event);
				});
				$('.fc-day').each(function() {
					// Get current day
					var day = moment.utc($(this).data('date'));
					// if this day has an event
					var event_count = 0;
					while(events.length && events[0].start.diff(day, 'days')===0) {
						event_count++;
						// this work because the events are sorted, and we only ever take the first
						// one from the array
						var event = events.shift();
						var $day = $(this);
						if ($day.data('events')) {
							$day.data('events').push(event);
						} else {
							$day.data('events', [event]);
						}
					}
					// draw a number w/ num of events for that day
					if (event_count > 0) {
						var $cal_day = $(this);
						// create a new canvas element the size of the cal day
						var $canvas = $('<canvas id="canvas-'+
							day.format('YYYY-M-DD') +
							'" class="'+ 
							"canvas-day text-center center-block" + 
							'" height="'+ 
							($cal_day.height()-13)+
							'" width="'+
							$cal_day.width()+
							'" data-count="'+
							event_count+
							'"></canvas>');
						$cal_day.html($canvas);
						drawCircle($canvas.get(0));
					}
				});
			},
			error: function() {
				addMessage('Error getting events', 'danger');
			},
		},
		eventRender: function(event, element) {
			// don't show the fullcalendar events
			return false;
		},
		eventAfterAllRender: function(view) {
		},
		// eventClick: function(calEvent, jsEvent, view) {
		// 	eventData = {
		// 		id: calEvent.id,
		// 		title: calEvent.title,
		// 		start: calEvent.start.toJSON(),
		// 		end: calEvent.end.toJSON(),
		// 		all_day: calEvent.allDay,
		// 	};
		// 	console.log(calEvent);
		// 	$event = $(jsEvent.target).parents('.fc-event-container');
		// 	console.log($event);
		// 	console.log($event[0]);
		// 	console.log($($event[0]));
		// 	$event.popover('show');
		// 	// deleteEvent(eventData);
		// 	// $('#calendar').fullCalendar('removeEvents', calEvent.id);
		// 	return false;
		// },
		timezone: 'local',
	});

	/*****************
	 * popover stuff *
	 *****************/
	$('#calendar').on('mouseenter', '.canvas-day', function() {
		$(this).popover({
			trigger: "focus",
			placement: 'auto top',
			html: true,
			content: function() {
				var $fcDay = $(this).parents('.fc-day');
				var $event_list = $('#events-popover-content').clone();
				var $item_proto = $event_list.find('.list-group-item').clone();
				$event_list.find('.list-group-item').remove();
				var $list_group = $event_list.find('.list-group');
				var format_string = 'ddd MMM DD, YYYY';
				$.each($fcDay.data('events'), function(index, event) {
					var $item = $item_proto.clone();
					$item.find('.event-title').text(event.title);
					$item.find('.event-description').text(event.description);
					$item.find('.event-date').text(event.start.format(format_string));
					$item.find('.event-time').text(event.start.format('hh:mm a'));
					$item.find('.event-class').text(event.course);
					$item.find('.event-id').text(event.id);
					$item.css('box-shadow', '1px 1px 0px 1px' + event.color);
					$list_group.append($item);
				});
				// add event for new edit cal button
				// this is how the modal gets events in it
				var $modal = $('#event-edit-modal');
				$modal.data('events', $fcDay.data('events'));

				return $event_list.html();
			},
			container: 'body',
		});
		$('.popover').remove();
		$(this).popover('show');

		$('.event-edit-link').click(function() {
			var pk = $(this).parents('.list-group-item').children('.event-id').text();
			var $modal = $('#event-edit-modal');
			$modal.data('event-id', pk);
			$modal.modal('show');
		});
	});

	// this is the script used on the user popover which seems to work well
	// it allows you to hover over the popover and it remains triggered
	// then when the mouse leaves, the popover disappears
	// I tried to combine this with the function above but couldn't get it to work cleanly

	// $('#calendar').on('mouseenter', '.canvas-day', function() {
	// $(this).popover({
	// 	trigger: "manual",
	// 	placement: 'auto top',
	// 	html: true,
	// 	content: function() {
	// 		return $('#events-popover-content').html();
	// 	},
	// 	container: 'body',
	// })
 //    .on("mouseenter", function () {
 //        var _this = this;
 //        $(this).popover("show");
 //        $(".popover").on("mouseleave", function () {
 //            $(_this).popover('hide');
 //        });
 //    })
 //    .on("mouseleave", function () {
 //        var _this = this;
 //        setTimeout(function () {
 //            if (!$(".popover:hover").length) {
 //                $(_this).popover("hide");
 //            }
 //        }, 100);
 //    });


	// click on date w/ events on it
	$('#calendar').on('click', '.canvas-day', function(event) {
		// why? why does this one need a stop propagation, and the mouseover will break if you do
		// that. seriously, wtf
		event.stopPropagation();
		$(this).popover({
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
		$(this).popover('show');
	});

	// close the popovers when you click outside
	// this is add to the body so it can be registered
	// with dynamically added popovers
	$('body').on('click', function (event) {
		var $target = $(event.target);
		// this makes baby pandas around the world cry salty tears
		if(!($target.hasClass('btn') ||
				 $target.hasClass('day') ||
				 $target.hasClass('date') ||
				 $target.hasClass('fc-day') ||
				 $target.hasClass('popover-title') ||
				 $target.hasClass('popover-content') ||
				 $target.hasClass('datepicker-switch') ||
				 $target.hasClass('datepicker-days') ||
				 $target.hasClass('table-condensed') ||
				 $target.hasClass('prev') ||
				 $target.hasClass('next') ||
				 $target.hasClass('dow') ||
				 $target.is('span') ||
				 $target.is('a') ||
				 $target.hasClass('form-control')
				)) {
			$('.popover').popover('hide');
		}
		// when you click on any of the list items in the drop down
    	$("#calSelect > li a").click(function(){
			// replace the cal icon with the title of the calendar
	        $(".cal-name").text($(this).text() + ' ');
	        $(".cal-name").data('calendar', $(this).data('calendar'));
    	});

    	// initialize date picker
		$('input.date').datepicker({
			format: "D M d, yyyy", //"yyyy-m-d"
		    startDate: "today",
			autoclose: true,
			todayHighlight: true
	    }).on('changeDate', function(event) {
			var date = event.date;
			date.setUTCHours(0,0,0,0);
			var pick = moment.utc(date);
			$('.date-input').data('date', pick);
		});
	});

	// submitting the form in the event creation popover
	$('body').on('submit', '#add-event-form', function(event) {
		var $form = $(event.target);
		var url = '/calendar/events/add/';
		var messages = [];
		data = '';

		// which calendar this event is for 
		var cal = $('.cal-name').data('calendar');
		data += "calendar=" + encodeURIComponent(cal);

		var date = $('.date-input').data('date');
		events = {};
		var title = $form.find('input[name=title]').val();
		var description = $form.find('input[name=description]').val();
		// don't bother sending empty entries
		// make a new event
		var newEvent = {
			'title': title,
			'description': description,
			'date': date.toJSON(),
			'hasTime': false,
		};
		events[0] = newEvent;
		events = JSON.stringify(events);
		data += "&events=" + encodeURIComponent(events);

		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			success: function(data) {
				messages = data.messages;
				// add the event to the calendar
				var event = JSON.parse(data.event);
				$cal = $('#calendar');
				$cal.fullCalendar('renderEvent', event[0].fields);

				var iso = moment(date).format('YYYY-M-DD');
				var $canvas = $('#canvas-'+iso);
				var count = parseInt($canvas.data('count')) + 1;
				$canvas.data('count', count);
				drawCircle($canvas);
			},
			fail: function(data) {
				addMessage('Failed to save event', 'danger');
			},
			complete: function(data) {
				$.each(messages, function(index, message){
					addMessage(message.message, message.extra_tags);
				});
			},

		});
		$('.popover').popover('hide');
		return false;
	});

	//Create cal event with button
	$('#createOptions').popover({
		trigger: 'manual',
		placement: 'bottom',
		html: true,
		// viewport: '#calendar',
		title: function() {
			return $('#newEventTitle').html();
		},
		content: function() {
			return $('#newEventContent').html();
		},
		container: 'body',
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

	// change the title when the view changes
	$('.cal-button').click(function() {
    	$('.cal-date').text(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});

	//toggle calendar list section
    $('.viewCals').on('click', function () {
        $('.flip-holder').toggleClass("flip");
    });

});

var saveEvent = function (eventData, create) {
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
			$.each(data.messages, function(index, message){
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

var deleteCalendar = function(cal_pk) {
	var messages = [];
	$.ajax({
		url: '/calendar/delete/',
		type: 'POST',
		data: {
			'id': cal_pk,
		},
		dataType: 'json',
		success: function(data) {
		},
		fail: function(data) {
		},
		complete: function(data) {
			messages = data.responseJSON.messages;
			$.each(messages, function(index, message){
				addMessage(message.message, message.extra_tags);
			});
		},
	});
};
var drawCircle = function(canvas) {
	var count = $(canvas).data('count');

	if (canvas.getContext){
		var ctx = canvas.getContext('2d');
		ctx.clearRect(0, 0, canvas.width, canvas.height);

		ctx.beginPath();
		var x              = $(canvas).width() / 2;               // x coordinate
		var y              = $(canvas).height() / 2;               // y coordinate
		var radius         = $(canvas).width() / 4.5;                    // Arc radius
		var startAngle     = 0;                     // Starting point on circle
		var endAngle       = Math.PI * 2; // End point on circle
		var anticlockwise  = true; // clockwise or anticlockwise

		ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise);

		ctx.fillStyle="#4C9ED9";
		ctx.fill();
		ctx.fillStyle="#FFFFFF";

		var font_x = parseInt(y*(2/3)).toString();
		ctx.font = font_x  + "pt Arial";
		var text_start = ctx.measureText(count);
		ctx.fillText(count, x-text_start.width/2, y + (y*(1/4)));
  }
};
