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
	 * Deleting documents
	 */
	// when the user clicks on the remove link, send ajax request
	var $delete_button = $('.delete-button');
	$delete_button.click(function() {
		// document pk is stored in the link itself with html5 data-* attribute
		var pk = $(this).data('document');
		var messages = [];
		$.ajax({
			url: '/documents/remove/',
			type: 'POST',
			data: {'document': pk,},
		})
		// success
		.done(function(data) {
			// fade out the class, remove from the dom, and add messages to message list
			messages = data.messages;
			$('#document_' + pk).fadeOut(300, function() {
				$(this).remove();
				$document_list = $('#document-list');
				// show the "you're not selling documents" message
				if($document_list.children().length < 1) {
					$('#no-documents').show();
				}
				// decrement number of uploaded documents
				$count = $('#upload-count');
				count = parseInt($count.html());
				$count.html(count - 1);
			});
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
	});

	/*
	 * Remove documents from purchased list
	 */
	var $remove = $('.remove-button');
	$remove.click(function() {
		// document pk is stored in the link itself with html5 data-* attribute
		var pk = $(this).data('document');
		var messages = [];
		$.ajax({
			url: '/documents/unpurchase/',
			type: 'POST',
			data: {'document': pk,},
		})
		// success
		.done(function(data) {
			// fade out the class, remove from the dom, and add messages to message list
			messages = data.messages;
			$('#purchased_' + pk).fadeOut(300, function() {
				$(this).remove();
				$purchased_list = $('#purchased-list');
				// show the "you haven't bought any documents" message
				if($purchased_list.children().length < 1) {
					$('#no-purchases').show();
				}
				// decrement number of purchased documents
				$count = $('#purchase-count');
				count = parseInt($count.html());
				$count.html(count - 1);
			});
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
