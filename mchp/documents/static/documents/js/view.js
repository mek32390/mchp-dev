$(function(){
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
	 * posting a review 
	 */
	// when the user clicks on the remove link, send ajax request
	var $submit_review = $('#submit-review');
	$submit_review.click(function() {
		$vote = $('#vote option:selected');
		$review = $('#review-comment');
		// document pk is stored in the link itself with html5 data-* attribute
		var pk = $(this).data('document');
		var messages = [];
		$.ajax({
			url: '/documents/review/',
			type: 'POST',
			data: {
				'document': pk,
				'review': $review.val(),
				'vote': 1,
			},
		})
		// success
		.done(function(data) {
			messages = data.messages;
		})
		.fail(function(data) {
			messages = data.responseJSON.messages;
		})
		.always(function() {
			// reguardless of success or failure, show messages to user
            $.each(messages, function (i, item) {
                addMessage(item.message, item.extra_tags);
            });
		});
		return false;
	});
});

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
