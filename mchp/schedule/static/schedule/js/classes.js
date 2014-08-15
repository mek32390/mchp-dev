/*
 * classes.js
 *
 * This file handles functionality for classes
 */
$(function() {
	var $toggleLink = $(this);
	var fetched = $toggleLink.data('fetched');
	if(fetched === true) {
		return;
	}
	var course = $toggleLink.data('course');
	var $calTab = $('#browse-tab-'+course);

	var messages = [];
	$.ajax({
		url: '/calendar/list/',
		type: 'GET',
		data: {
			'course': course,
		},
		dataType: 'json',
		success: function(data) {
			var $calList =  $calTab.find('.calendar-item-list');
			$('#calendar-count-'+course).text(data.calendars.length);

			if(data.hasOwnProperty('calendars') && data.calendars.length > 0) {
				var subscriptions = $('.subscription-list').map(function(index, element){
					return $(element).find('label').data('cal');
				}).get();
				$.each(data.calendars, function(index, calendar) {
					var $calendar = $calList.find('.calendar-item-proto').clone();
					$calendar.removeClass('hidden');
					$calendar.removeClass('calendar-item-proto');
					$calendar.find('.calendar-title').text(calendar.title);
					$calendar.find('.calendar-title').attr('href', '/calendar/preview/'+calendar.pk);
					$calendar.find('.calendar-picture-link').attr('href', '/calendar/preview/'+calendar.pk);
					$calendar.find('.calendar-uploader').attr('href', '/profile/'+calendar.owner);
					$calendar.find('.calendar-uploader').text(calendar.owner__user__username);
					if(subscriptions.indexOf(calendar.pk) > -1) {
						$calendar.find('.calendar-browse-price').html(calendar.price + ' lemons ' + $calendar.find('.calendar-browse-price').html());
					} else {
						$calendar.find('.calendar-browse-price').text(calendar.price + ' lemons');
					}
					$calendar.find('.calendar-subscriptions').text(' ' + calendar.subscriptions + ' followers');
					$calendar.find('.calendar-event-count').text(calendar.events);
					$calendar.find('.calendar-create-date').text(moment.utc(calendar.date).from(moment.utc()));
					if(calendar.accuracy >= 0) {
						$calendar.find('.calendar-accuracy').text(calendar.accuracy + '% Accurate');
					}
					$calendar.find('.calendar-professor').text(calendar.course__professor);
					$calendar.find('.calendar-time').html(calendar.time);
					$calList.append($calendar);
				});
			} else {
				$calList.html('<hr><p class="lead">There are no calendars for this course yet. That means no competition for you. <a href="/calendar/create">Create the first Calendar</a> right now and make some money! </p><hr>');
			}
			$toggleLink.data('fetched', true);
		},
		fail: function(data) {
		},
		complete: function(data) {
			$.each(messages, function(index, message){
				addMessage(message.message, message.extra_tags);
			});
		},
	});
});
