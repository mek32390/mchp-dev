/*
 * school.js
 *
 * This file handles functionality for a public school page
 */
$(function() {
	var courses = ["ECON 200", "ACCT 200", "MGMT 300", "MKTG 361", "CSC 400", "CSC 230"];
	$('.typeahead').typeahead({
		source: courses
	});
});
