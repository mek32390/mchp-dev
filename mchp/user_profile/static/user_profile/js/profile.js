$(function(){
	// show profile info when friend button clicked (example)
	$('#friend_button').click(function () {
		$('#top_friends').removeClass('hidden');
		$('#top_achievements').removeClass('hidden');
		$('#user_classes').removeClass('hidden');
		$('#friend_message').addClass('hidden');
		$('#shared_classes').addClass('hidden');
	});
	//giving each score section a tooltip on user's total score
	$('#score_1').tooltip({
    'show': true,
        'placement': 'bottom',
        'title': "Score 1"
	});

	$('#score_2').tooltip({
    'show': true,
        'placement': 'bottom',
        'title': "Score 2"
	});

	$('#score_3').tooltip({
    'show': true,
        'placement': 'bottom',
        'title': "Score 3"
	});
	// animating the score bar
	$('#score_1').css({'width':'35%', 'transition':'width 1.5s ease 0s'});
	$('#score_2').css({'width':'35%', 'transition':'width 2s ease 0s'});
	$('#score_3').css({'width':'30%', 'transition':'width 2.5s ease 0s'});

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
    });

	//button to trigger about field (not used right now)
    $('#edit-button').click(function(e) {
    e.stopPropagation();
    $('#about').editable('toggle');
	
	});

});
