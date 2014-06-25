$(function(){
	$("#resend_form").submit(function() {

		var url = "/login/resend-email/"; // page just for handing resend requests

		$.ajax({
			type: "POST",
			url: url,
			data: $("#resend_form").serialize(), 
			dataType: "json",
			success: function(data) {
				$('.resend_confirm').html('<p>Verification Email resent.</p>');
			},
			error: function(data) {
				$('.resend_confirm').html('<p>Resend request failed.</p>');
			}
		});

		return false; 
	});
});
