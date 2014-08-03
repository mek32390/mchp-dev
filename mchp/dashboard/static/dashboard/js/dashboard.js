$(function(){
	//make breadcrumbs sortable
	$(".breadcrumb").sortable ({ 
		cancel: '#weather_data',
		placeholder: 'ql-placeholder',
		containment: ".breadcrumb",
		scroll: false
	});
	//make a breadcrumb not clickable when dragging
	$( ".breadcrumb" ).disableSelection();

	//toggle news categories section
	$('#edit_sections').on('click', function () {
    	$('.flip-holder').toggleClass("flip");
	});
});
