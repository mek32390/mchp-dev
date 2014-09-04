/*
 * dashboard-tour.js
 *
 * This file handles the tour shown to first time users on the dashboard.
 */
 $(function() {

	// Instance the tour
	var tour = new Tour({

		onShow: function(tour) {
	        $('.people-section').removeClass('animated bounceInUp');
	        $('.pulse-section').removeClass('animated bounceInUp');
	        $('.stories-section').removeClass('animated bounceInUp');
	        // $('a').addClass('disabled');
    	},

		name: "dashboard-tour",
		storage: false,
		backdrop: true,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [
		{
			path: "/home",
			orphan: true,
			title: "<strong>Welcome home, Mitch</strong>",
			content: "This is your homepage within a homepage. It could be the first of it\'s kind, but who knows... Your homepage takes activity from all over mchp and organizes it for you so you'll always know what's going on in your classes, and your life.",
		},
		{
			path: "/home",
			element: "#ref-alert",
			title: "<strong>Your Referral Code</strong>",
			content: 'Read above, it\'s important. Your unique referral code is <strong>"CODE"</strong>. You also have a unique referral link. Both can be accessed from your Account Settings page (top right of the page).',
			placement: "bottom",
		},
		{
			path: "/home",
			element: ".breadcrumb",
			title: "<strong>Your Quicklinks</strong>",
			content: "Click on a link and it will open in a new tab. It's that easy.",
			placement: "bottom"
		},
		{
			path: "/home",
			element: ".today-section",
			title: "<strong>Your Events</strong>",
			content: "Each day, we'll check to see if you have any events in your calendar for that day, and if you do, you'll see them here.",
			placement: "right"
		},
		{
			path: "/home",
			element: ".people-section",
			title: "<strong>Your Peers</strong>",
			content: "You'll see your classmates, friends, and fellow mchp users here.",
			placement: "right"
		},
		{
			path: "/home",
			element: ".pulse-section",
			title: "<strong>Your Pulse</strong>",
			content: "The Pulse is a feed of everything important going on in your classes and mchp. You'll see things like when someone joins a class you're in, or when a document or calendar is created.",
			placement: "right"
		},
		{
			path: "/home",
			element: ".stories-section",
			title: "<strong>Your Stories</strong>",
			content: "You can choose what stories to follow by customizing your interests (<i class='fa fa-bars'></i>). We've got plenty to choose from, so have at it after we're done with this tour.",
			placement: "left",
			onShown: function() {
	        	$('.stories-section').css({'height':'90%'});
	        	$('#news-scroll').css({'height':'90%'});
    		}
		},
		{
			path: "/home",
			element: ".step-2",
		    title: "<strong>What would you like to do next?</strong>",
		    content: "Click the <i class='fa fa-book'></i> (book) to go to your classes, or the <i class='fa fa-calendar'></i> (calendar) to go to your calendar.",
		    placement: "bottom",
		    reflex: "true"
		}
	]});

	// Initialize the tour
	tour.init();
	// Start the tour
	tour.start();
});
