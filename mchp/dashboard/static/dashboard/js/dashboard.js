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
		$('#news-'+setting).toggleClass('hidden');

		$.ajax({
			url: '/home/toggle-rss/',
			type: 'POST',
			data: {
				'setting': setting,
			},
		});
		fetchRss();
		if ($('.news-list-item:visible').length === 0) {
			$('.news-list-empty').removeClass('hidden');
		}
	});

	window.pulse = new Pulse({
	});
	window.pulse.setup();
	fetchFeed();
	fetchRss();
	var now = moment($('.current-time').data('time'));
	startTime(now._tzm);
});

var fetchRss = function() {
	if ($('.news-list-item:visible').length !== 0) {
		$('.news-list-empty').addClass('hidden');
	}
	
	var $sections = $('.news-group');
	$sections.each(function(index, section) {
		var $section = $(section);
		if($section.hasClass('hidden')) {
			return true;
		}
		// clear old items if any
		$('.news-item:not(.news-item-proto)').remove();
		var $links = $section.find('.news-item-proto');
		$links.each(function(index, link) {
			var $link = $(link);
			var $section = $link.parents('.news-group');
			var url = $link.data('link') ;
			var name = $link.data('name');
			var count = $link.data('count');
			var successFn = function(feed) {
				for(var i = 0 ; i < count ; i++) {
					addRss($section, feed.items[i], name);
				}
			};
			$.getFeed({
				url: '/home/rss-proxy/',
				data: {
					'url': url,
				},
				success: successFn,
			});
		});
	});
};

var addRss = function(section, rss, name) {
	if (!rss) {
		return;
	}
	var $item = $('.news-item-proto').first().clone();
	$item.removeClass('news-item-proto');
	$item.removeClass('hidden');
	var time = moment(rss.updated, 'ddd, DD MMM YYYY HH:mm:ss ZZ');

	var $content = $item.find('.news-content');
	$item.find('.news-headline').html(rss.title);
	$item.find('.news-headline').attr('href', rss.link);

	// um
	// this is so that resources inside the html are not fetched,
	// resulting in wasted bandwidth and mixed content on the page
	var dom = '<!DOCTYPE html><html><head></head><body>'+rss.description +'</body></html>';
	var doc = new DOMParser().parseFromString(dom, 'text/html');
	var description = doc.body.textContent;

	if (description.length > 200) {
		var $continueLink = $('<a>[...]</a>');
		$continueLink.attr('href', rss.link);
		$content.text(description.substr(0,200).trim());
		$content.append($continueLink);
	} else {
		$content.text(description);
	}
	$item.find('.news-time').text(time.fromNow());
	$item.find('.news-name').text(name);
	section.append($item);
};

var processFeed = function(feed) {
	var items = [];
	$.each(feed, function(index, itemData) {
		var title = '';
		var link = '/school/course/'+itemData.course__pk;
		if (itemData.event__title !== null) {
			title = itemData.event__title;
			link = '/calendar/';
		} else if (itemData.document__title !== null) {
			title = itemData.document__title;
			link = '/documents/'+itemData.document__uuid + '/' + title;
		}
		var item = new PulseItem({
			type: itemData.type,
			course: {
				'name': itemData.course__dept + ' ' + itemData.course__course_number,
				'pk': itemData.course__pk,
			},
			target: {
				'name': itemData.student__user__username,
				'pk': itemData.student__pk,
			},
			time: moment.utc(itemData.time),
			title: title,
			link: link,
		});
		items.push(item);
	});
	return items;
};

var PulseItem = function(options) {
	this.type = options.type;
	this.time = options.time;
	this.target = options.target;
	this.course = options.course;
	this.title = options.title;
	this.link = options.link;
};

var Pulse = function(options) {
};

Pulse.prototype.setup = function() {
	var self = this;
};

Pulse.prototype.addItem = function(item) {
	var $pulse = $('#pulse');
	var $node = $('.' + item.type+'-proto').clone();

	$node.removeClass(item.type+'-proto');
	$node.removeClass('hidden');

	$node.find('.dash-title').text(item.title);
	$node.find('.dash-title-link').attr('href', item.link);

	$node.find('.dash-time').text(item.time.fromNow());

	$node.find('.dash-target').text(item.target.name);
	$node.find('.dash-target').parents('a').attr('href', '/profile/' + item.target.pk);

	$node.find('.dash-course').text(item.course.name);
	$node.find('.dash-course').parents('a').attr('href', '/school/course/'+item.course.pk+'/'+item.course.name);

	$pulse.append($node);
};

Pulse.prototype.render = function(items) {
	var self = this;

	$('.dash-load').remove();
	$.each(items, function(index, item) {
		self.addItem(item);
	});
	if (items.length < 1) {
		$('.dash-empty').removeClass('hidden');
	}
};

var fetchFeed = function() {
	var feed = [];
	$.ajax({
		url: '/home/feed/',
		type: 'GET',
		success: function(data) {
			items = processFeed(data.feed);
			pulse.render(items);
		},
		fail: function(data) {
			addMessage("Pulse not found. He's dead jim.");
		},
		complete: function(data) {
			return feed;
		},
	});
};

function startTime(zone) {
    var now = moment().zone(zone);
    $('.current-time').html(now.format('h:mm a'));
    var t = setTimeout(function(){
		startTime(zone);
	}, 1000);
}
