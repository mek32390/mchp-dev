/*
 * dashboard.js
 *
 * This file handles functionality for dashboard
 */

$(function(){

 	/*
	/*
	/* TOUR FUNCTIONS
	/*
	*/


	// Instance the tour
	var tour = new Tour({

		onStart: function(tour) {
	        $('#people-section').removeClass('animated bounceInUp');
	        $('#pulse-section').removeClass('animated bounceInUp');
	        $('#stories-section').removeClass('animated bounceInUp').css('height','690px');
	        $('.alert-link').css('pointer-events','none');
	        $('.flip-holder div').css({'-webkit-backface-visibility':'hidden','backface-visibility':'hidden'});
    	},

		name: "dashboard-tour",
		backdrop: true,
		// storage: false,
		template: "<div class='popover tour'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div><nav class='popover-navigation'><div class='btn-group'><button class='btn btn-default btn-sm' data-role='prev'>« Prev</button><button class='btn btn-default btn-sm' data-role='next'>Next »</button></div><button class='btn btn-default btn-end btn-sm tour-btn-end' data-role='end'>End tour</button></nav></div>",
		steps: [
		{
			path: "/home",
			orphan: true,
			title: "<strong>Welcome home, " + MCHP_USERNAME + "</strong>",
			content: "This is your homepage. We've customized it just for you, and it puts everything you need, all in one place.",
		},
		{
			path: "/home",
			element: "#ref-alert",
			title: "<strong>Your Referral Code</strong>",
			content: 'Read above, it\'s important.',
			placement: "bottom",
		},
		{
			path: "/home",
			element: "#quicklinks",
			title: "<strong>Your Quicklinks</strong>",
			content: "Click on a link and it will open in a new tab. It's that easy.",
			placement: "bottom"
		},
		{
			path: "/home",
			element: "#today-section",
			title: "<strong>Your Events</strong>",
			content: "Each day, we'll check to see if you have any events that day, and if you do, you'll see them here.",
			placement: "right"
		},
		{
			path: "/home",
			element: "#people-section",
			title: "<strong>Your Peers</strong>",
			content: "You'll see your classmates, friends, and fellow mchp users here.",
			placement: "right"
		},
		{
			path: "/home",
			element: "#pulse-section",
			title: "<strong>Your Pulse</strong>",
			content: "The Pulse is a feed of everything important going on in your classes and mchp.",
			placement: "right"
		},
		{
			path: "/home",
			element: "#stories-section",
			title: "<strong>Your Stories</strong>",
			content: "You can choose what stories to follow by customizing your interests (<i class='fa fa-bars'></i>). We've got plenty to choose from, so have at it after we're done with this tour.",
			placement: "left"
		},
		{
			path: "/home",
			element: ".step-2",
		    title: "<strong>What\'s next, " + MCHP_USERNAME + "?</strong>",
		    content: "Click the <i class='fa fa-book'></i> (book) to go to your classes, or the <i class='fa fa-calendar'></i> (calendar) to go to your calendar.",
		    placement: "bottom",
		    reflex: "true"
		}
	]});

	// Initialize the tour
	tour.init();
	// Start the tour
	tour.start();

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
	$('.pulse-con').css('max-height',$(window).height() - 100);
	$('#news-scroll').css('max-height',$(window).height() - 100);

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
	$item.find('.news-time').text(time.fromNow());
	$item.find('.news-name').text(name);

	// um
	// this is so that resources inside the html are not fetched,
	// resulting in wasted bandwidth and mixed content on the page
	var dom = '<!DOCTYPE html><html><head></head><body>'+rss.description +'</body></html>';
    if (!DOMParser) {
        section.append($item);
        return;
    }
	var doc = new DOMParser().parseFromString(dom, 'text/html');
	var description = doc.body.textContent;

	if (description.length > 200) {
		var $continueText = $('<span>...</span>');
		// $continueLink.attr('href', rss.link);
		$content.text(description.substr(0,200).trim());
		$content.append($continueText);
	} else {
		$content.text(description);
	}
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
		} else if (itemData.calendar__title !== null) {
			title = itemData.calendar__title;
			link = '/calendar/preview/' + itemData.calendar__pk + '/';
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
