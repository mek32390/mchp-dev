$(function() {
	// show email log in form when clicked
	$('#show-login').on('click', function () {
		$('#facebookLogin').fadeOut(250, function () {
			$('.emailLogin').fadeIn(500);
		});
	});

	// hide unwanted labels
	$('label[for="id_login"]').hide();
	$('label[for="id_password"]').hide();

	// make error messages into actual messages
	var $list = $('.errorlist').first();

	$list.children().each(function() {
		addMessage($(this).text(), 'danger');
	});
	$('.errorlist').remove();

	// Convert form to BS Validator
	$("#id_login").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
	$("#id_login").before( "<span class='input-group-addon'><i class='fa fa-user fa-fw'></i></span>" );
	$("#id_login").addClass("form-control input-lg");

	$("#id_password").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
	$("#id_password").before( "<span class='input-group-addon'><i class='fa fa-lock fa-fw'></i></span>" );
	$("#id_password").addClass("form-control input-lg");

	// don't collaspe the manual signup when the page refreshes 
    if(document.referrer === document.URL) {
        $('#facebookLogin').fadeOut(1, function () {
            $('.emailLogin').show();
        });
    }

	// BS Validator 
	$('#login_form').bootstrapValidator({
		feedbackIcons: {
			valid: 'glyphicon glyphicon-ok',
			invalid: 'glyphicon glyphicon-remove',
			validating: 'glyphicon glyphicon-refresh'
		},
		fields: {
			login: {
				trigger: 'keyup',
				validators: {
					notEmpty: {
						message: 'This field is required'
					},
					stringLength: {
						min: 4,
						message: 'Your username or email must be more than 4 characters'
					}
				}
			},
			password: {
				trigger: 'keyup',
				validators: {
					notEmpty: {
						message: 'This field is required'
					},
				}
			}
		}
	});
});
