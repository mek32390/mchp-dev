$(function() {
	// automatically fill and submit the email field
	hidden_email = $('.signup input[name=saved_email]').attr('value');
	$('#id_username').attr('value', 'charles'+Date.now());
	// if this fails once, it will just show this page as it is
	if(hidden_email !== '' && document.referrer !== document.URL) {
		$('body').hide();
		$('#id_email').attr('value', hidden_email);
		$('.signup').submit();
	}
});
