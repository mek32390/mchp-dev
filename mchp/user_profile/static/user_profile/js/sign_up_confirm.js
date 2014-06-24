$(function() {
	// automatically fill and submit the email field
	hidden_email = $('.signup input[name=saved_email]').attr('value');
	if(hidden_email !== '') {
		$('body').hide();
		$('#id_email').attr('value', hidden_email);
		$('.signup').submit();
	}
});
