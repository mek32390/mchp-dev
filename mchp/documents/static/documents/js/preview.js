$(function () {
    // show email sign up input when clicked
    $('#show-signup').on('click', function () {
        $('#login-options').fadeOut(250, function () {
            $('#email-signup').fadeIn(500).removeClass('hidden');
        });
    });
	$('.facebook').click(function() {
		$('#mchp-login-prompt').modal('hide');
		$(window).on('focus', function() {
			document.location.reload();
		});
	});

    //validate signup form 
    $('#email-signup').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            email: {
                trigger: 'keyup',
                validators: {
                    notEmpty: {
                        message: 'This field is required'
                    },
                    emailAddress: {
                        message: 'Please enter a valid email address'
                    },
                    regexp: {
                        regexp: /(\.edu)$/,
                        message: 'Only .edu emails allowed'
                    }
                }
            }
        }
    });
	$('#buy-form').on('submit', function() {
		if ($('.student-points').length < 1) {
			return true;
		}
		var docPrice = parseInt($('#document-price').text());
		var points = parseInt($('.student-points').text());
		var afterBalance = points|0 - docPrice|0;
		if (afterBalance > 0) {
			return true;
		} else {
			$('#points-modal').modal('show');
			return false;
		}
	});
});
