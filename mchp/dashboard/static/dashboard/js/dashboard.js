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

	// using jquery.cookie plugin
	var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	// csrf token stuff
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	$('#ref-alert').on('close.bs.alert', function  () {
		toggle_flag('referral_info');
	});
	$('.pulse-con').css('max-height',$(window).height() - 200);
});
