/*
 * upload_doc.js
 * 
 * This file is for the custom browse file feature
 */
$(function() {
	// convert select to nice input
	$("#id_course").addClass("form-control input-lg");
	// $("#id_document").addClass("form-control input-lg");
	// convert browse file button to BS3 button
	$('.btn-file :file').on('fileselect', function(event, numFiles, label) {
        
        var input = $(this).parents('.input-group').find(':text'),
            log = numFiles > 1 ? numFiles + ' files selected' : label;
        
        if( input.length ) {
            input.val(log);
        } else {
            if( log ) alert(log);
        }
        
    });
});

// provide feedback on browse file button
$(document).on('change', '.btn-file :file', function() {
  var input = $(this),
      numFiles = input.get(0).files ? input.get(0).files.length : 1,
      label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});

