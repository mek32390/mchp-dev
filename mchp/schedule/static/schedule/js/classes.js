/*
 * classes.js
 *
 * This file handles functionality for classes
 */

$(function() {

	/*
	/*
	/* TOUR FUNCTIONS
	/*
	*/

	// Instance the tour
	var tour = new Tour({

		name: "classes-tour",
		backdrop: true,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [
		{
			path: "/classes",
			orphan: true,
		    title: "<strong>Here are your Classes, Mitch!</strong>",
		    content: 'All of your classes on a single page. We like to call it, "simple."'
		},
		{
			path: "/classes",
			element: "ul.nav-tabs",
		    title: "<strong>Switch between Classes</strong>",
		    content: "Each of your class's has it's own tab.",
		    placement: "bottom",
		    onShown: function() {
	        	$('body > ul > li:nth-child(2').addClass('disabled').css('pointer-events','none');
	        	$('body > ul > li:nth-child(3').addClass('disabled').css('pointer-events','none');
	        	$('body > ul > li:nth-child(4').addClass('disabled').css('pointer-events','none');
	        	$('body > ul > li:nth-child(5').addClass('disabled').css('pointer-events','none');
	        	$('body > ul > li:nth-child(6').addClass('disabled').css('pointer-events','none');
	        	$('body > ul > li:nth-child(7').addClass('disabled').css('pointer-events','none');
    		}
		},
		{
			path: "/classes",
			element: "#course1 > .well ",
		    title: "<strong>Class Information</strong>",
		    content: "Clicking the title of your class will take you to a public course page, where you can see all the documents and calendars associated with the entire course. Same goes for your college or university.",
		    reflex: true,
		    placement: "bottom"
		},
		{
			path: "/classes",
			element: "#course1 > div.row > div.col-sm-5.animated > div:nth-child(1)",
		    title: "<strong>Class Activity</strong>",
		    content: "See what's going on in your class, literally. All of the class's activity will show up here.",
		    placement: "right"
		},
		{
			path: "/classes",
			element: "#course1 > div.row > div.col-sm-5.animated > div:nth-child(2)",
		    title: "<strong>Classmates</strong>",
		    content: "A list of all of your classmates",
		    placement: "right"
		},
		{
			path: "/classes",
			element: "#course1 > div.row > div.col-sm-7.animated > div",
		    title: "<strong>Class Documents</strong>",
		    content: "Each time a document is uploaded, it will appear here, including any you upload.",
		    placement: "left"
		},
		{
			path: "/classes",
			element: ".step-2",
		    title: "<strong>What would you like to do next?</strong>",
		    content: "Click the <i class='fa fa-home'></i> (home) icon above to go to your homepage, or the <i class='fa fa-calendar'></i> (calendar) to go to your calendar.",
		    placement: "bottom",
		    reflex: true
		}
		
	]});

	// Initialize the tour
	tour.init();
	// Start the tour
	tour.start();


	/*
	/*
	/* IDK WHAT THESE FUNCTIONS ARE FOR? CALENDAR PAGE? RANDOM
	/*
	*/


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
