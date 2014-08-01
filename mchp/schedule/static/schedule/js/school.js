$(function() {
	$('#class-search').typeahead([
		{
			name: 'countries',
			remote: window.location.pathname,
		}
	]);
});
