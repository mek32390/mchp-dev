/*
 * school.js
 *
 * This file handles functionality for a public school page
 */

$(function() {
	$('#class-search').typeahead([
		{
			name: 'countries',
			remote: window.location.pathname,
		}
	]);
});
