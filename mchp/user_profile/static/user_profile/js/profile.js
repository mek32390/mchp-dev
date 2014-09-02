$(function(){

	// show profile info when friend button clicked (example)
	// $('#friend_button').click(function () {
	// 	$('#top_friends').removeClass('hidden');
	// 	$('#top_achievements').removeClass('hidden');
	// 	$('#user_classes').removeClass('hidden');
	// 	$('#friend-message').addClass('hidden');
	// 	$('#shared_classes').addClass('hidden');
	// });

	//animating achievement scores
	// $('#documentMasterScore').css({'width':'30%', 'transition':'width 2.5s ease 0s'});

	//giving each achievement type a score tooltip 
	// $('#documentMasterScore').tooltip({
 //    'show': true,
 //        'placement': 'bottom',
 //        'title': "30%"
	// });

	//xeditable options
	$('#about').editable({
    	mode: 'inline',
    	inputclass: 'input-lg',
		url: '/profile/edit-blurb/',
		unsavedclass: 'text-danger',
		emptyclass: '',
		emptytext: 'Add a blurb about yourself here!',
		highlight: '',
		onblur: 'submit',				
		send: 'always',
    });

	// this should really only be done when you first click on the editable
	$.ajax({
		url: '/school/department/',
		type: 'GET',
		success: function(data) {
			var majors = $.map(data.majors, function(major, index) { 
				return major.name;
			});
			$('#major').editable({
				mode: 'inline',
				unsavedclass: 'text-danger',
				emptyclass: '',
				emptytext: 'Select your major',
				highlight: '',
				onblur: 'submit',				
				send: 'always',
				showbuttons: false,
				url: '/profile/edit-major/',
				typeahead: {
					local: majors,
				}
			});
		},
	});

	$('#pic-input').change(function() {
		var form = $('#pic-form').get(0);
		$.ajax({
			url: '/profile/edit-pic/',
			data: new FormData(form),
			processData: false,
			contentType: false,
			type: 'POST',
			success: function(data) {
				$('.profile-image').attr('src', data.url);
				addMessage('Your latest internet persona has been given wings', 'success');
			},
		});
	});

});
