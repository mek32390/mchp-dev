//Signup form show/hide
$(function () {
	// show manual login forms
	$('#show-signUp').on('click', function () {
		$('.facebookSignup').fadeOut(250, function () {
			$('.form-group').fadeIn(500);
		});
		$('.signup').fadeIn(500);
		$('.email_reminder').fadeIn(500);
	});

	// this is to add the session stored email address, and hide that field
	$('.email_reminder').hide();
	hidden = $('.signup input[name=saved_email]').attr('value');
	if(hidden !== ''){
		$('#id_email').hide();
		$('label[for=id_email]').hide();
		$('#id_email').attr('value', $hidden);
	} else if(hidden === '') {
		// if there is no session email, this will show the e-mail input field
		$('.email_reminder h4').html("Sign up with E-mail")
	}
});
