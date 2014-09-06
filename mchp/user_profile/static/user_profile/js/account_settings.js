$(function() {
	// http or https needs to match the site requesting this resource
	if (typeof ZeroClipboard !== 'undefined') {
		ZeroClipboard.config( { swfPath: "https://ajax.cdnjs.com/ajax/libs/zeroclipboard/2.1.5/ZeroClipboard.swf" } );

		var client = new ZeroClipboard($(".copy-button").get(0) );
		client.on("aftercopy", function(){
			$copy = $('#code-button');
			$copy.addClass('btn-success btn');
			$copy.html('copied');
		});
		var second = new ZeroClipboard($(".copy-button").get(1) );
		second.on("aftercopy", function(){
			$copy = $('#link-button');
			$copy.addClass('btn-success btn');
			$copy.html('copied');
		});
	}
});
