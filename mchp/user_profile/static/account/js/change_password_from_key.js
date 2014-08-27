$(function() {

	// hide unwanted labels
	$('label[for="id_password1"]').hide();
	$('label[for="id_password2"]').hide();

	// change placeholder text on form inputs
	$('#id_password1').attr('placeholder','New Password')
	$('#id_password2').attr('placeholder','Repeat it please')


	// style error message to BS Validator
	var html = [], $list = $('.errorlist');

	html.push('<div class="errorlist">');
	$list.find('li').each(function() {
		html.push('<p class="text-danger small">' + $(this).text() + '</p>');
	});
	html.push('</div>');
	$list.replaceWith(html.join(''));

	// Convert form to BS Validator
	$("#id_password1").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
	$("#id_password1").before( "<span class='input-group-addon'><i class='fa fa-lock fa-fw'></i></span>" );
	$("#id_password1").addClass("form-control input-lg");

	$("#id_password2").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
	$("#id_password2").before( "<span class='input-group-addon'><i class='fa fa-lock fa-fw'></i></span>" );
	$("#id_password2").addClass("form-control input-lg");

	// BS Validator 
	$('#change-password').bootstrapValidator({
		feedbackIcons: {
			valid: 'glyphicon glyphicon-ok',
		invalid: 'glyphicon glyphicon-remove',
		validating: 'glyphicon glyphicon-refresh'
		},
		fields: {
			password1: {
				trigger: 'keyup',
				validators: {
					notEmpty: {
					message: 'Please enter a new password'
					},
					stringLength: {
                        min: 8,
                        message: 'Please make your password at least 8 characters'
                    }
				}
			},
			password2: {
				trigger: 'keyup',
				validators: {
					notEmpty: {
					message: 'Please repeat your password'
					},
					identical: {
                        field: 'password1',
                        message: 'The password should be the same as above'
                    }
				}
			}
		}
	});
});
