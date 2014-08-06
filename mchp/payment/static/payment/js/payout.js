$(function() {
	var $form = $('.cash-out-form');

	$form.submit(function(event) {
		var messages = [];
		$.ajax({
			url: payout_url,
			type: 'POST',
			data: $form.serialize(),
			success: function(data) {
				messages = data.messages;
				$('.savings-amount').text('0.00');
				$('.modal').modal('hide');
			},
			error: function(data) {
				$('.modal').modal('hide');
				messages = data.responseJSON.messages;
			},
			complete: function(data) {
				$.each(messages, function(index, message){
					addMessage(message.message, message.extra_tags);
				});
			},
		});
		return false;
	});
});
