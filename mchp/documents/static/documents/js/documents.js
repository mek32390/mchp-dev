$(function(){
	// http or https needs to match the site requesting this resource
	if (typeof ZeroClipboard != 'undefined') {
		ZeroClipboard.config( { swfPath: "http://ajax.cdnjs.com/ajax/libs/zeroclipboard/2.1.5/ZeroClipboard.swf" } );

		var client = new ZeroClipboard(document.getElementById("copy-button") );
		client.on("aftercopy", function(){
			// $('.copy-message').html("&#x2714; Link copied.").delay(2000).fadeOut(600);
			$('.copy-message').html("&#x2714; Link copied.");
		});
	}
	/* fb stuff */
	window.fbAsyncInit = function(){
		FB.init({
			appId: '1488225931413638',
		status: true,
		cookie: true,
		xfbml: true 
		}); 
	};
	(function(d, debug) {
		var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
		if (d.getElementById(id)) {
			return;
		}
		js = d.createElement('script'); 
		js.id = id;
		js.async = true;
		js.src = "//connect.facebook.net/en_US/all" + (debug ? "/debug" : "") + ".js";
		ref.parentNode.insertBefore(js, ref);
	}(document, /*debug*/ true));

	function postToFeed(title, desc, url, image){
		var obj = {
			method: 'feed',
			link: url, 
			picture: image,
			name: title,
			description: desc
		};
		function callback(response){}
		FB.ui(obj, callback);
	}
	$('.btnShare').click(function(){
		elem = $(this);
		postToFeed(elem.data('title'), elem.data('desc'), elem.prop('href'), elem.data('image'));

		return false;
	});
});
