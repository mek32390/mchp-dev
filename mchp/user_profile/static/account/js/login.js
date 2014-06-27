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

	// style error message to BS Validator
	var html = [], $list = $('.errorlist');

	html.push('<div class="errorlist">');
	$list.find('li').each(function() {
		html.push('<p class="text-danger small">' + $(this).text() + '</p>');
	});
	html.push('</div>');
	$list.replaceWith(html.join(''));

	// Convert form to BS Validator
	$("#id_login").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
	$("#id_login").before( "<span class='input-group-addon'><i class='fa fa-user fa-fw'></i></span>" );
	$("#id_login").addClass("form-control input-lg");

	$("#id_password").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
	$("#id_password").before( "<span class='input-group-addon'><i class='fa fa-lock fa-fw'></i></span>" );
	$("#id_password").addClass("form-control input-lg");

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
