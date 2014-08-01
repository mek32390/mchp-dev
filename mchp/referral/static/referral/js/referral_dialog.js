/* 
 * This file gets loaded by the referral modal template tag
 */
$(function() {
	$form = $('#referral-form');
	$form.submit(function() {
		var messages = [];
		$.ajax({
			url: dialog_url,
			type: 'POST',
			data: $form.serialize(),
			success: function(data) {
				messages = data.messages;
			},
			fail: function(data) {
				addMessage('Failed to redeem promo code', 'danger');
			},
			complete: function(data) {
				$.each(messages, function(index, message){
					addMessage(message.message, message.extra_tags);
				});
			},
		});
		$modal.modal('hide');
		$('#referral-input').val('');
		return false;
	});
});
