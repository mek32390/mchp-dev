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
  // Upload Doc Form Validation
  $('#upload_form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        // Set default threshold for all fields. It is null by default
        threshold: 3,
        fields: {
            title: {
                validators: {
                    notEmpty: {
                        message: 'Please provide a title'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9 | ]+$/i,
                        message: 'The title code can only consist of alphabetical characters, spaces, and numbers'
                    },
                    stringLength: {
                        min: 5,
                        max: 50,
                        message: 'The title should be at least 5 characters long'
                    }
                }
            },
            description: {
                validators: {
                    notEmpty: {
                        message: 'Please provide a description'
                    },
                    stringLength: {
                        min: 10,
                        max: 200,
                        message: 'The description should be at least 10 characters'
                    }
                }
            },
            course: {
                validators: {
                    notEmpty: {
                        message: 'Please choose which course this document belongs to'
                    },
                }
            },
            price: {
                validators: {
                    notEmpty: {
                        message: 'Please set this selling price of this document'
                    },
                    between: {
                        min: 1,
                        max: 1000000000,
                        message: 'The price must be between 0 and 1 billion!'
                    }
                }
            },
            document: {
                validators: {
                    notEmpty: {
                        message: 'Please select a file to upload'
                    }
                }
            }
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
