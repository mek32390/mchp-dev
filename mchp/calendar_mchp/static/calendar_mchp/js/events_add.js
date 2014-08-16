/*
 * events_add.js
 *
 * This file handles the functionality of the calendar events add page and bootstrap xeditable
 */
$(function() {

	// template tutorial
	$('.step-one-next').on('click', function () {
		$('.step-one').fadeOut(250, function () {
    		$('.step-two').fadeIn(500);
    		$('.step-two').removeClass('hidden');
    	});
	});

	$('.step-two-next').on('click', function () {
		$('.step-two').fadeOut(250, function () {
    		$('.step-three').fadeIn(500);
    		$('.step-three').removeClass('hidden');
    	});
	});

	$('.step-three-next').on('click', function () {
		$('.step-three').fadeOut(250, function () {
    		$('.step-four').fadeIn(500);
    		$('.step-four').removeClass('hidden');
    	});
	});

	$('.step-four-next').on('click', function () {
		$('.template-tutorial').fadeOut(250, function () {
    		$('.table').fadeIn(500);
    		$('.table').removeClass('hidden');
			$('.event-button').removeClass('hidden');
    	});
	});

	var activeCalendar = null;
	//display dropdown selection 
	$(".dropdown-menu li a").click(function(event){
		var pk = $(this).data('cal');
		//display the selected calendar in the button
		$(".btn:first-child").html($(this).html());
		$(".btn:first-child").val($(this).text()).append(" <span class='caret'></span>");
		//bring the course info and template into view once calendar is selected
		$('.course-info').hide();
		$('#course-info-'+pk).fadeIn(500).removeClass('hidden');
		$('.templates').fadeIn(700).removeClass('hidden');
		// $('button.hidden').fadeIn(700).removeClass('hidden');

		// get rid of the table rows that already exist (but not the proto one which is hidden)
		$('.templates').children('table').children('tbody').children('.event-template:visible').remove();

		// each calendar has its own days and end date, this is an awful way to get them
		var end_date = window['end_date_'+pk];
		var meeting_days = window['meeting_days_'+pk];

		// add a row for every day between today and the end of the calendar
		var days = moment.twix(moment.utc(), end_date).iterate("days");
		var $event_table = $('.templates').children('table').children('tbody');
		while(days.hasNext()) {
			var day = days.next();
			// don't include days that aren't part of the schedule
			if($.inArray(day.isoWeekday(), meeting_days) > -1) {
				add_event_template(day, $event_table);
			}
		}
		// add one last row for last day of class
		var $last = $('<tr class="last-event event-template">' + 
				'<td colspan="4" class="event-title"><span><strong>Last day of Class: ' + moment.utc(end_date).format('MMMM Do') +'<strong></span></td>' + 
				'</tr>');
		$event_table.append($last);
		// make the newly added fields editable
		$(".editField").editable({
			type: "text",
			showbuttons: false,
			anim: "fast",
			onblur: 'cancel'  
		});

		// when you press enter, select the next editable
		$('.editable').on('hidden', function(e, reason){
			if(reason === 'save' || reason === 'nochange') {
				var $td_link = $(this);
				var $next;
				// go to the next column
				if ($td_link.parent().hasClass('event-title')) {
					$next = $td_link.closest('td').next().find('.editable');
				} else {
					// go to the next row
					$next_row = $td_link.parent().closest('tr').next();
					$next = $next_row.find('.event-title').find('a');
				}
				$next.editable('show');
			}
		});

		activeCalendar = pk;
	});

	//turn to inline mode
	$.fn.editable.defaults.mode = 'inline';
	//make editable field empty but still have a visible length
	var empty_text = '';
	for(var i = 0 ; i < 40; i++) {
		empty_text += '&nbsp;';
	}
	$.fn.editable.defaults.emptytext = empty_text;

	// on first page load, if a cal was just made, show it
	if (typeof selected_calendar !== 'undefined' ){
		var $selectedCalendar = $('#select-calendar-'+selected_calendar);
		if($selectedCalendar.length > 0) {
			$selectedCalendar.click();
			activeCalendar = selected_calendar;
		}
	}

	/*********************
	 * Submit all events *
	 *********************/
	$('.event-button').click(function() {
		var url = '/calendar/events/add/';
		var messages = [];
		// which calendar this event is for 
		var cal = activeCalendar;
		data = "";
		data += "calendar=" + encodeURIComponent(cal);
		events = {};

		$('.event-template').each(function(index){
			var $row = $(this);
			var date = $row.data('date');
			// don't send the proto type or last day row
			if(!date) {
				return;
			}
			// get only unsaved text (no big huge lines of empty space from the empty text thing)
			var title = $row.children('.event-title').children('.editable-unsaved').text();
			var description = $row.children('.event-description').children('.editable-unsaved').text();
			// don't bother sending empty entries
			if (!$row.find('.editable').hasClass('editable-unsaved')) {
				return;
			}
			// make a new event
			var event = {
				'title': title,
			'description': description,
			'date': date.toJSON(),
			'hasTime': false,
			};
			events[index] = event;
		});
		events = JSON.stringify(events);
		data += "&events=" + encodeURIComponent(events);

		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			dataType: 'json',
			success: function(data) {
				messages = data.messages;
				window.location.href = "/calendar/";
			},
			fail: function(data) {
				messages = data.responseJSON.messages;
			},
			complete: function(data) {
				$.each(messages, function(index, message){
					addMessage(message.message, message.extra_tags);
				});
			},

		});
	});
});

var add_event_template = function(date, table) {
	var $event_template = $('#proto-event-template').clone();
	$event_template.removeClass('hidden');
	$event_template.children('.event-date').text(date.format('MMMM Do'));
	$event_template.children('.event-day').text(date.format('ddd'));
	$event_template.data('date', date);

	table.append($event_template);
};