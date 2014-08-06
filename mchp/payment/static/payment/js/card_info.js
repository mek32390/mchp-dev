$(function() {

	var $cardOptions = $('.card-options');
	$('.card-options').html("<span class='pull-right small'>Set as <span class='btn btn-xs btn-default'><i class='fa fa-check text-primary'></i></span> <span class='btn btn-xs btn-default'><i class='fa fa-money text-success'></i></span> <span class='btn btn-xs btn-default'><i class='fa fa-times text-danger'></i></span></span>");

	$('input[type=radio][name=user-cards]').change(function() {
        if (this.value == 'option1') {
 				alert("#1");
        }
        else if (this.value == 'option2') {
        	$('#optionsRadios2').next('.label').addClass('.text-danger');
            alert("#2");
        }
    });
	

	var $form = $('.card-form');
	// for credit card fancy form 
	$form.card({
    	container: '.card-wrapper', // *required*
    	numberInput: 'input[name=number]',
    	nameInput: 'input[name=name]',
    	expiryInput: 'input[name=expiry]',
    	cvcInput: 'input[name=cvc]',
    	width: 350,
	});

	$form.submit(function(event) {
		// clear errors
		$('.payment-errors').text('');
		// Disable the submit button to prevent repeated clicks
		$form.find('button').prop('disabled', true);
		var expiry = $('.cc-expiry').val().split('/');
		exp_month = parseInt(expiry[0]);
		exp_year = parseInt(expiry[1]);
		if (isNaN(exp_month)){
			exp_month = 13;
		}
		if (isNaN(exp_year)){
			exp_year = 1970;
		}
		var card_data = {
			name: $('.cc-name').val(),
			number: $('.cc-number').val(),
			cvc: $('.cc-cvc').val(),
			exp_month: exp_month,
			exp_year: exp_year,
		};

		Stripe.card.createToken(card_data, function(status, response) {

			if (response.error) {
				// Show the errors on the form
				$('.payment-errors').text(response.error.message);
				$('.cc-submit-button').prop('disabled', false);
			} else {
				// response contains id and card, which contains additional card details
				var token = response.id;
				// Insert the token into the form so it gets submitted to the server
				$form.append($('<input type="hidden" name="stripeToken" />').val(token));
				// don't send the server the actual cc info
				// $('.no-send').val('');
				// and submit
				var messages = [];
				$.ajax({
					url: card_info_url,
					type: 'POST',
					data: $form.serialize(),
					success: function(data) {
						messages = data.messages;
						$('.modal').modal('hide');
						// clear the modal of its values
						$('.no-send').val('');
					},
					error: function(data) {
						res = data.responseJSON.response;
						$('.payment-errors').text(res);
						$('.cc-submit-button').prop('disabled', false);
					},
					complete: function(data) {
						$.each(messages, function(index, message){
							addMessage(message.message, message.extra_tags);
						});
					},
				});
			}
		});

		// Prevent the form from submitting with the default action
		return false;
	});
});
