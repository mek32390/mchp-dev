$(function(){

	/*
	/*
	/* TOUR FUNCTIONS
	/*
	*/

	// Instance the first tour
	var tour = new Tour({
		onStart: function() {
			$('.profile-image').removeClass('animated flipInX delayed-sm');
		},

		name: "profile-tour",
		backdrop: true,
		// storage: false,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [

		{
			element: "#profile-header",
			backdrop: false,
		    title: "<strong>Here is your Page, " + MCHP_USERNAME + "!</strong>",
		    content: "Edit your <strong>Picture</strong>, <strong>Username</strong>, <strong>Major</strong>, and <strong>Blurb</strong> by clicking on them.",
		    placement: "bottom",
		    reflex: true
		}
		
	]});

	// Initialize the tour
	tour.init();
	// Start the tour
	tour.start();

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
		emptyclass: 'text-danger',
		emptytext: 'Add a blurb about yourself here!',
		highlight: '',
		onblur: 'submit',				
		send: 'always',
    });

	$('#profile-username').editable({
    	mode: 'inline',
    	inputclass: 'input-lg',
		url: '/profile/edit-username/',
		unsavedclass: 'text-danger',
		emptyclass: 'text-danger',
		emptytext: 'Change your username',
		highlight: '',
		onblur: 'submit',				
		send: 'always',
		success: function(data) {
			addMessage('You shall henceforth be known as ' + data.username, 'success');
		},
		error: function(response, newvalue) {
			addMessage('Tough luck, someone already has that username!', 'danger');
			return '';
		},
    });

	// this should really only be done when you first click on the editable
	$.ajax({
		url: '/school/major/',
		type: 'GET',
		success: function(data) {
			var majors = $.map(data.majors, function(major, index) { 
				return major.name;
			});
			$('#major').editable({
				mode: 'inline',
				unsavedclass: 'text-danger',
				emptyclass: 'text-danger',
				emptytext: 'Select your major',
				highlight: 'text-success',
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
