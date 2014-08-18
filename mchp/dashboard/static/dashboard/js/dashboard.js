$(function(){

 	/*
	/*
	/* NEWS FUNCTIONS
	/*
	*/


	//toggle news categories section on click
	$('#edit-sections').on('click', function () {
		$('.flip-holder').toggleClass("flip");
	});

	//scrollspy news section 
	$("#news-scroll").scrollspy({
		target: "#news-navbar"
	});

    // set var for news section nav link click adjustment
    var offset = 1000;

    $('#news-navbar .nav li a').click(function (event) {
    	event.preventDefault();

		var $link = $(this);
		var setting = $link.data('setting');

    	$('#news-'+setting).get(0).scrollIntoView();
		scrollBy(0, -offset);

		$('.news-list-item').removeClass('active');
		$link.parents('li').addClass('active');

    });

	/*
	 * QUICKLINKS FUNCTIONS SEEM TO BE CAUSING A LOT OF TROUBLE 
	 * SO I MOVED THEM DOWN HERE AND COMMENTED THEM OUT
	 */

	//make breadcrumbs sortable
	// $(".breadcrumb").sortable ({ 
	// 	cancel: '#weather_data',
	// 	placeholder: 'ql-placeholder',
	// 	containment: ".breadcrumb",
	// 	scroll: false
	// });
	//make a breadcrumb not clickable when dragging
	// $( ".breadcrumb" ).disableSelection();

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
		toggle_flag($(this).data('event'));
	});
	$('.pulse-con').css('max-height',$(window).height() - 200);

	$('.toggle-rss').click(function() {
		var setting = $(this).data('setting');

		$('#news-list-item-'+setting).toggleClass('hidden');
		// console.log($('#news-list-item-'+setting));
		$('#news-'+setting).toggleClass('hidden');

		$.ajax({
			url: '/dashboard/toggle-rss/',
			type: 'POST',
			data: {
				'setting': setting,
			},
		});
	});
	$('.news-header').each(function(index, header){
		$(header).css('background-color', Please.make_color());
		$(header).css('color', '#fff');
	});
	var candidateColor = Please.make_color();
	console.log(candidateColor);
});
