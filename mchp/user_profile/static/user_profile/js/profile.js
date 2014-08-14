$(function(){

	// show profile info when friend button clicked (example)
	$('#friend_button').click(function () {
		$('#top_friends').removeClass('hidden');
		$('#top_achievements').removeClass('hidden');
		$('#user_classes').removeClass('hidden');
		$('#friend-message').addClass('hidden');
		$('#shared_classes').addClass('hidden');
	});

	//animating achievement scores
	$('#documentMasterScore').css({'width':'30%', 'transition':'width 2.5s ease 0s'});

	//giving each achievement type a score tooltip 
	$('#documentMasterScore').tooltip({
    'show': true,
        'placement': 'bottom',
        'title': "30%"
	});

	//xeditable options
	$('#about').editable({
    	mode: 'inline',
    	inputclass: 'input-lg',
		url: '/profile/edit-blurb/',
		unsavedclass: 'text-danger',
		emptyclass: '',
		emptytext: 'Add a blurb abut yourself!',
		highlight: '',
		onblur: 'submit',				
		send: 'always',
    });

  $('#major').editable({
    	mode: 'inline',
    	inputclass: '',
		url: '/profile/edit-major/',
		unsavedclass: 'text-danger',
		emptyclass: '',
		emptytext: 'Add your Major',
		highlight: '',
		onblur: 'submit',				
		send: 'always',
    });

	//button to trigger about field (not used right now)
	$('#edit-button').click(function(e) {
		e.stopPropagation();
		$('#about').editable('toggle');

	});

});
