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
});
