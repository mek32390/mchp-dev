$(function(){
	var $schools = $('#school-list');
	$schools.hide();

	$('#nope').click(function() {
		$('#college_select').fadeOut(250, function () {
			$schools.show();
			$schools.fadeIn(500);
		});
	});

	//choose college from list if user picks one
	$('#college-form2').change(function() {
		$("#join-college").removeAttr("disabled");  
	});
});
