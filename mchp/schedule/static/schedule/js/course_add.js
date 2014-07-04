/*
 * course_add.js
 *
 * This file handles the removeal of classes from the enrolled class list, using ajax.
 */
$(function() {
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
	// when the user clicks on the drop link, send ajax request
	$('.enrolled-class-id').find('a').click(function() {
		// course number is stored in the link itself with html5 data-* attribute
		var course = $(this).data('course');
		var messages = []
		$.ajax({
			url: '/school/course/remove/',
			type: 'POST',
			data: {'courses': course,},
		})
		.done(function(data) {
			// fade out the class, remove from the dom, and add messages to message list
			messages = data.messages;
			$('#enrolled_' + course).fadeOut(300, function() {
				$(this).remove();
				$class_list = $('#enrolled_list');
				if($class_list.children().length < 1) {
					$class_list.append("No classes added to your schedule yet.")
				}
			});
		})
		.fail(function(data) {
			addMessage("Failed to drop course", "fail")
		})
		.always(function() {
			// reguardless of success or failure, show messages to user
            $.each(messages, function (i, item) {
                addMessage(item.message, item.extra_tags);
            });
		});
	});
});

function addMessage(text, extra_tags) {
    var message = $(
		'<div class="alert alert-' + extra_tags + ' alert-dismissible" role="alert">\
			<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>\
			<ul class="messages">\
				<li class="' + extra_tags + '">' + text + '</li>\
			</ul>\
		</div>');
    $(".django-messages").append(message);
}
