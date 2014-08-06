$(function() {
	var $form = $('.purchase-points');

	var card = $('.submit-card');
	var savings = $('.submit-savings');

	var purchase_type = '';
	var detect_purchase_type = function(type) {
		purchase_type = type;
	};
	card.click(function() {
		purchase_type = 'card';
		$form.submit();
	});
	savings.click(function() {
		purchase_type = 'savings';
		$form.submit();
	});

	$form.submit(function(event) {
		data = $form.serialize();
		type = JSON.stringify(purchase_type);
		data += "&type=" + encodeURIComponent(type);
		var messages = [];
		$.ajax({
			url: purchase_url,
			type: 'POST',
			data: data,
			success: function(data) {
				messages = data.messages;
				$('.savings-amount').text(data.balance);
				$('.student-points').text(data.points);
				$('.modal').modal('hide');
			},
			error: function(data) {
				addMessage('Failed to charge card', 'danger');
			},
			complete: function(data) {
				$.each(messages, function(index, message){
					addMessage(message.message, message.extra_tags);
				});
			},
		});

		// Prevent the form from submitting with the default action
		return false;
	});
});
