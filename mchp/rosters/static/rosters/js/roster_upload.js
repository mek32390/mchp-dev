/*
 * upload_roster.js
 * 
 * This file is for the roster upload page
 */

$(function() {

	// Bootstrap Editable form fields

	// make the newly added fields editable
	$(".editField").editable({
		type: "text",
		mode: "inline",
		showbuttons: false,
		anim: "fast",
		onblur: 'cancel'  
	});

	$('.examSelect').editable({
		type: "select",
		mode: "inline",
		showbuttons: false,
		anim: "fast",
		onblur: 'cancel', 
        value: 1,    
        source: [
              {value: 1, text: 'Exam 1'},
              {value: 2, text: 'Exam 2'},
              {value: 3, text: 'Exam 3'}
           ]
    });

    $('.rosterCode').editable({
        type: "textarea",
        inputclass: "input-sm",
        placeholder: "Command + v here to paste",
		mode: "inline",
		showbuttons: false,
		anim: "fast",
		onblur: 'cancel',
        rows: 1
    });
		
});



