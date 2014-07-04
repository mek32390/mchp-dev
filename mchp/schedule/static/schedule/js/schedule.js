/*
 * This file is for js things that are app wide, and should be on all schedule app pages
 */

$(function() {
	/* messages */
	$messages = $('.django-messages');
	// fade messages that were added on page load
	$messages.children('div').delay(5000).fadeOut(500, function(){
		$(this).remove();
	});

	/* 
	 * When messages are appended dynamically, they should fade out too
	 */
	// create an observer instance
	var observer = new MutationObserver(function(mutations) {
		mutations.forEach(function(mutation) {
			var $nodes = $(mutation.addedNodes);
			$nodes.delay(5000).fadeOut(500, function(){
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
});
