/*
 * course_add_tour.js
 *
 * This file handles the tour shown to first time users on the course add page
 */
$(function() {

	// Instance the first tour
	var tour1 = new Tour({
		name: "addclass-tour-1",
		storage: false,
		backdrop: true,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [

		{
			path: "/school/course/add/",
			orphan: true,
		    title: "<strong>Welcome!</strong>",
		    content: "This is your class schedule page, where you can add and drop classes from your schedule. Your schedule looks empty, so let's start off by adding some classes to it.",
		    backdrop: "true"
		},
		{
			path: "/school/course/add/",
			element: "#class_search_form",
		    title: "<strong>Search for a Class</strong>",
		    content: "Enter a <strong>Course Code</strong> and <strong>Number</strong>, then hit Enter!",
		    placement: "bottom",
		    reflex: true
		    // onHidden: function (tour1) {tour1.end()}
		}

	]});

	// Initialize the tour
	tour1.init();
	// Start the tour
	tour1.start();




	// Instance the second tour
	var tour2 = new Tour({
		name: "addclass-tour-2",
		storage: false,
		backdrop: true,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [
		
		{
			path: "/school/course/add/",
			orphan: true,
		    title: "<strong>Nice work!</strong>",
		    content: "Now that you've added a class to your schedule, we can explore the rest of mchp!",
		    backdrop: "true"
		},
		{
			path: "/school/course/add/",
			element: ".step-2",
		    title: "<strong>What would you like to do next?</strong>",
		    content: "<p>Click the <i class='fa fa-home'></i> (home) icon above to go to your homepage, the <i class='fa fa-book'></i> (book) to go to your classes, or the <i class='fa fa-calendar'></i> (calendar) to go to your calendar.</p><p class='small'>Click 'End Tour' to continue adding classes to your schedule. You can add/drop classes from your schedule anytime.</p>",
		    placement: "bottom",
		    reflex: true
		}

	]});


	$('.join').on('click', function () {
		// Initialize the tour
		tour2.init();
		// Start the tour
		tour2.start();
	});
});
