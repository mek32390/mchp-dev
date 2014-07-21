$(function(){
	$(".breadcrumb").sortable ({ 
		cancel: '#weather_data',
		placeholder: 'ql-placeholder',
		containment: ".breadcrumb",
		scroll: false
	});
	$( ".breadcrumb" ).disableSelection();
});
