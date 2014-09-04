/*
 * calendar-tour.js
 *
 * This file handles the tour shown to first time users on the calendar page
 */
$(function() {
	
	// Instance the tour
	var tour = new Tour({

		name: "calendar-tour",
		storage: false,
		backdrop: true,
		path: "/calendar",
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [
		{
			orphan: true,
		    title: "<strong>Your Calendar(s)</strong>",
		    content: 'Here\'s how mchp calendars work: You can make a calendar for each of the classes you are in. For instance, you can make an "ECON 200" calendar, and put assignment due dates, tests, and projects in it.'
		},
		{
			orphan: true,
		    title: "<strong>Private Calendar</strong>",
		    content: "If you choose to make your ECON 200 Calendar private, only you will be able to see the events in it, just like a regular calendar- for your eyes only."
		},
		{
			orphan: true,
		    title: "<strong>Selling a Calendar</strong>",
		    content: "If you choose to sell it, your classmates will be able to subscribe to it for a fee, and they will get to see all of the events you add to it, rate it, and get notified whenever you change something on it. For every classmate that subscribes to it, you'll make money by the week.</li></ul>"
		},
		{
			element: ".owned-cals-section",
		    title: "<strong>Calendars You Own</strong>",
		    content: "This is where the calendars you create will appear, regardless if you are selling them or not.",
		    placement: "right"
		},
		{
			element: ".following-cals-section",
		    title: "<strong>Calendars You Follow</strong>",
		    content: "This is where the calendars you subscribe to will appear.",
		    placement: "right"
		},
		{
			element: ".view-cals-btn",
		    title: "<strong>Browse Calendars to Follow</strong>",
		    content: "This is where your classmates' calendars that they choose to sell will appear.",
		    placement: "left"
		},
		{
			element: ".step-2",
		    title: "<strong>What would you like to do next?</strong>",
		    content: "Click the <i class='fa fa-home'></i> (home) icon above to go to your homepage, or the <i class='fa fa-book'></i> (book) to go to your classes.",
		    placement: "bottom",
		    reflex: true
		}
		
	]});

	// Initialize the tour
	tour.init();
	// Start the tour
	tour.start();
});
