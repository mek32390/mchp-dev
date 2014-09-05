/*
 * course_add.js
 *
 * This file handles the removeal of classes from the enrolled class list, using ajax.
 */

$(function() {

	/*
	/*
	/* TOUR FUNCTIONS
	/*
	*/

	// Instance the first tour
	var tour1 = new Tour({
		name: "addclass-tour-1",
		backdrop: true,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [

		{
			path: "/school/course/add/",
			orphan: true,
		    title: "<strong>Welcome!</strong>",
		    content: "This is your class schedule page, where you can add and drop classes from your schedule. Your schedule looks empty, so let's start off by adding some classes to it.",
		    backdrop: "true"
		},
		{
			path: "/school/course/add/",
			element: "#class_search_form",
		    title: "<strong>Search for a Class</strong>",
		    content: "Enter a <strong>Course Code</strong> and <strong>Number</strong>, then hit Enter!",
		    placement: "bottom",
		    reflex: true
		    // onHidden: function (tour1) {tour1.end()}
		}

	]});

	// Initialize the tour
	tour1.init();
	// Start the tour
	tour1.start();


	// Instance the second tour
	var tour2 = new Tour({
		name: "addclass-tour-2",
		storage: false,
		backdrop: true,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [
		
		{
			path: "/school/course/add/",
			orphan: true,
		    title: "<strong>Nice work!</strong>",
		    content: "Now that you've added a class to your schedule, we can explore the rest of mchp!",
		    backdrop: "true"
		},
		{
			path: "/school/course/add/",
			element: ".step-2",
		    title: "<strong>What would you like to do next?</strong>",
		    content: "<p>Click the <i class='fa fa-home'></i> (home) icon above to go to your homepage, the <i class='fa fa-book'></i> (book) to go to your classes, or the <i class='fa fa-calendar'></i> (calendar) to go to your calendar.</p><p class='small'>Click 'End Tour' to continue adding classes to your schedule. You can add/drop classes from your schedule anytime.</p>",
		    placement: "bottom",
		    reflex: true
		}

	]});


	$('.join').on('click', function () {
		// Initialize the tour
		tour2.init();
		// Start the tour
		tour2.start();
	});


	/*
	/*
	/* OTHER CLASS ADDING/DROPPING FUNCTIONS
	/*
	*/


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

	/* 
	 * Enrolling in classes
	 */
	$('.list-group-item button').click(function(){
		$form = $(this).siblings('form');
		var button = $(this);
		$.ajax({
			url: '/school/course/add/',
			type: 'POST',
			data: $form.serialize(),
		})
		// success
		.done(function(data) {
			messages = data.messages;
			button.html('Enrolled');
			button.attr('disabled', true);
			addToClassList($.parseJSON(data.course)[0]);
			// remove the div that tells you you have no classes
			$('#no-classes').remove();
		})
		.fail(function(data) {
			addMessage("Failed to enroll in course", "fail");
		})
		.always(function() {
			// reguardless of success or failure, show messages to user
            $.each(messages, function (i, item) {
                addMessage(item.message, item.extra_tags);
			});
		});

		// don't actually sumbit the form with the button
		return false;
	});

	/*
	 * Dropping classes
	 */
	// when the user clicks on the drop link, send ajax request
	$('.enrolled-class-id').find('.drop-button').click(function() {
		// course number is stored in the link itself with html5 data-* attribute
		var course = $(this).data('course');
		var messages = [];
		$.ajax({
			url: '/school/course/remove/',
			type: 'POST',
			data: {'courses': course,},
		})
		// success
		.done(function(data) {
			// fade out the class, remove from the dom, and add messages to message list
			messages = data.messages;
			$('#enrolled_' + course).fadeOut(300, function() {
				$(this).remove();
				$class_list = $('#enrolled_list');
				if($class_list.children().length < 1) {
					$class_list.append('<div id="no-classes">No classes added to your schedule yet.</div>');
				}
			});
		})
		.fail(function(data) {
			addMessage("Failed to drop course", "fail");
		})
		.always(function() {
			// reguardless of success or failure, show messages to user
            $.each(messages, function (i, item) {
                addMessage(item.message, item.extra_tags);
            });
		});
	});
});

function addToClassList(course) {
	// csrf?
	var node = $(
		'<div class="list-group-item enrolled-class-id" id="enrolled_'+ course.pk +'">'+
			'<h4 class="list-group-item-heading">'+ course.fields.dept + ' ' + course.fields.course_number +
				'<small class="pull-right">'+
					'<!-- <a href="javascript:void(0)" class="badge" data-course="{{course.pk}}">drop</a> -->'+
				'</small>'+
			'</h4>'+
			'<p class="list-group-item-text">with Instructor ' + course.fields.professor + '</p>'+
		'</div>');
	$('#enrolled_list').append(node);
}

function addMessage(text, extra_tags) {
    var message = $(
		'<div class="alert alert-' + extra_tags + ' alert-dismissible" role="alert">' +
			'<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+
			'<ul class="messages">'+
				'<li class="' + extra_tags + '">' + text + '</li>'+
			'</ul>'+
		'</div>');
    $(".django-messages").append(message);
}
