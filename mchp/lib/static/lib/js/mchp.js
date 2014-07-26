/*
 * This is for things that should happen site wide
 */

$(function() {
	// style django error messages to mimic BS3
    var html = [],
        $list = $('.errorlist');

    html.push('<div class="errorlist">');
        $list.find('li').each(function() {
        html.push('<p class="text-danger small">' + $(this).text() + '</p>');
        });
    html.push('</div>');
    $list.replaceWith(html.join(''));
    
	/* messages */
	$messages = $('.django-messages');
	// fade messages that were added on page load
	$messages.children('div').delay(3000).addClass('animated bounceInRight').fadeOut(500, function(){
		$(this).remove();
	});

	/* When messages are appended dynamically, they should fade out too */
	// create an observer instance
	var observer = new MutationObserver(function(mutations) {
		mutations.forEach(function(mutation) {
			var $nodes = $(mutation.addedNodes);
			$nodes.delay(3000).addClass('animated bounceInRight').fadeOut(500, function(){
				$(this).remove();
			});
		});
	});
	// configuration of the observer:
	var config = { attributes: true, childList: true, characterData: true };
	// pass in the target node, as well as the observer options
	observer.observe($messages.get(0), config);

	/* custom scroll bar */
	// can be applied to any div
	$('.scrolls').enscroll({
		showOnHover: false,
		verticalTrackClass: 'track3',
		verticalHandleClass: 'handle3',
		scrollIncrement: 50,
	});

	// for credit card fancy form 
	$('#cardForm').card({
    	container: '.card-wrapper', // *required*
    	numberInput: 'input[name=number]',
    	nameInput: 'input[name=first-name]',
    	expiryInput: 'input[name=expiry]',
    	cvcInput: 'input[name=cvc]',

    	width: 350, // optional — default 350px
	});

	// hover opacity for score bar
	$('.score-bar').on( "mouseenter", function () {
		$(this).css({'transition':'opacity .5s ease 0s', 'opacity':'1'});
	});
	$('.score-bar').on( "mouseleave", function () {
		$(this).css({'transition':'opacity .5s ease 0s', 'opacity':'.5'} );
	});		
	//Score bar double click
	$('.score-bar').on( "dblclick", function () {
		// $('.score-breakdown').toggleClass('hidden').toggleClass('animated slideInRight');
		$('#score_1').toggleClass('hidden').toggleClass('animated slideInLeft');
		$('#score_2').toggleClass('hidden').toggleClass('animated slideInRight');
		$('#score_3').toggleClass('hidden').toggleClass('animated slideInRight');
		$('#level_score').removeClass('hidden').toggleClass('animated slideInLeft');
	});
	// score bar entrance on page load
	$('#score_1').css({'width':'35%', 'transition':'width 1.5s ease 0s'});
	$('#score_2').css({'width':'55%', 'transition':'width 2s ease 0s'});
	$('#score_3').css({'width':'10%', 'transition':'width 1s ease 0s'});

	//giving each score section a tooltip on user's total score
	$('#score_1').tooltip({
    'show': true,
        'placement': 'bottom',
        'title': "Score 1"
	});

	$('#score_2').tooltip({
    'show': true,
        'placement': 'bottom',
        'title': "Score 2"
	});

	$('#score_3').tooltip({
    'show': true,
        'placement': 'bottom',
        'title': "Score 3"
	});
});

function addMessage(text, extra_tags) {
    var message = $(
		'<div class="alert alert-' + extra_tags + ' alert-dismissible" role="alert">' +
			'<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+
			'<ul class="messages">'+
				'<li class="' + extra_tags + '">' + text + '</li>'+
			'</ul>'+
		'</div>');
    $(".django-messages").append(message);
}
