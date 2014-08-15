$(function() {
	// http or https needs to match the site requesting this resource
	if (typeof ZeroClipboard !== 'undefined') {
		ZeroClipboard.config( { swfPath: "http://ajax.cdnjs.com/ajax/libs/zeroclipboard/2.1.5/ZeroClipboard.swf" } );

		var client = new ZeroClipboard($("#copy-button") );
		client.on("aftercopy", function(){
			alert('what');
			$copy = $('#copy-button');
			$copy.attr('class', 'btn-success btn');
			$copy.html('<i class="fa fa-check-circle-o"></i> Now Paste it Somewhere!');
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
	}(document, /*debug*/ false));

	function postToFeed(title, desc, url){
		var obj = {
			method: 'feed',
			link: url, 
			name: title,
			description: desc,
			picture: 'https://s3-us-west-2.amazonaws.com/mchpstatic/Circle+Icons+/Custom/calendar-blank.svg',
		};
		console.log(obj);
		function callback(response){
		}
		FB.ui(obj, callback);
	}
	$('.btnShare').click(function(){
		elem = $(this);
		postToFeed(elem.data('title'), elem.data('desc'), elem.prop('href') );

		return false;
	});
});
