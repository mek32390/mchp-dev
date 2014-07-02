$(function() {
	// using jquery.cookie plugin
	var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	$('.enrolled-class-id').find('a').click(function() {
		var course = $(this).data('course');
		var messages = []
		$.ajax({
			url: '/school/course/remove/',
			type: 'POST',
			data: {'courses': course,},
		})
		.done(function(data) {
			messages = data.messages;
			$('#enrolled_' + course).fadeOut(300, function() {
				$(this).remove();
			});
		})
		.fail(function(data) {
			addMessage("Failed to drop course", "fail")
		})
		.always(function() {
            $.each(messages, function (i, item) {
                addMessage(item.message, item.extra_tags);
            });
		});
	});
});

function addMessage(text, extra_tags) {
    var message = $('<li class="'+extra_tags+'">'+text+'</li>');
    $(".messages").append(message);
}
