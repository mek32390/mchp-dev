/*
 * classes-tour.js
 *
 * This file handles the tour shown to first time users on the classes page
 */
$(function() {

	
	// Instance the tour
	var tour = new Tour({

		name: "classes-tour",
		storage: false,
		backdrop: true,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [
		{
			path: "/classes",
			orphan: true,
		    title: "<strong>Your Classes</strong>",
		    content: 'All of your classes on a single page. We like to call this, "easy and awesome."'
		},
		{
			path: "/classes",
			element: "ul.nav-tabs",
		    title: "<strong>Switch between Classes</strong>",
		    content: "Each of your class's has it's own tab.",
		    placement: "bottom",
		    onShown: function() {
	        	$('body > ul > li:nth-child(2').addClass('disabled').css('pointer-events','none');
	        	$('body > ul > li:nth-child(3').addClass('disabled').css('pointer-events','none');;
	        	$('body > ul > li:nth-child(4').addClass('disabled').css('pointer-events','none');;
	        	$('body > ul > li:nth-child(5').addClass('disabled').css('pointer-events','none');;
	        	$('body > ul > li:nth-child(6').addClass('disabled').css('pointer-events','none');;
	        	$('body > ul > li:nth-child(7').addClass('disabled').css('pointer-events','none');;
    		}
		},
		{
			path: "/classes",
			element: "#course1 > div.well.well-md",
		    title: "<strong>Class Information</strong>",
		    content: "If you click the title of your class, it will take you to the course page, where you can see all the documents and calendars associated with the course. Same goes for your college or university.",
		    reflex: true,
		    placement: "bottom"
		},
		{
			path: "/classes",
			element: "#course1 > div.row > div.col-sm-5.animated > div:nth-child(1)",
		    title: "<strong>Class Activity</strong>",
		    content: "See what's going on in your class, literally. All of the class's activity will show up here.",
		    placement: "right"
		},
		{
			path: "/classes",
			element: "#course1 > div.row > div.col-sm-5.animated > div:nth-child(2)",
		    title: "<strong>Classmates</strong>",
		    content: "A list of all of your classmates",
		    placement: "right"
		},
		{
			path: "/classes",
			element: "#course1 > div.row > div.col-sm-7.animated > div",
		    title: "<strong>Class Documents</strong>",
		    content: "Each time a document is uploaded, it will appear here, including any you upload.",
		    placement: "left"
		},
		{
			path: "/classes",
			element: ".step-2",
		    title: "<strong>What would you like to do next?</strong>",
		    content: "Click the <i class='fa fa-home'></i> (home) icon above to go to your homepage, or the <i class='fa fa-calendar'></i> (calendar) to go to your calendar.",
		    placement: "bottom",
		    reflex: true
		}
		
	]});

	// Initialize the tour
	tour.init();
	// Start the tour
	tour.start();
});
