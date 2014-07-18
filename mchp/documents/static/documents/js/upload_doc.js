/*
 * upload_doc.js
 * 
 * This file is for the custom browse file feature
 */

$(function() {

	// convert select to nice input
	$("#id_course").addClass("form-control input-lg");
	// convert default browse file to nice input
	$("#id_document").wrap("<div class='input-lg form-control'></div>").addClass("btn");
    // convert course select to column
    $("div.form-group:nth-child(4)").wrap("<div class='row'><div class='col-xs-8'></div></div>");
    // add hidden course search input to column
    $('div.form-group:nth-child(1)').before("<div class='form-group hidden' id='course_search_form'><div class='input-group'><span class='input-group-addon'><strong>Course Search:</strong></span><input type='text' placeholder='ex: ECON 200' class='form-control input-lg'></div></div>");
    // add browse class button in it's own column
    $("div.row:nth-child(4)").append("<div class='col-xs-4'><a href='#' id='course_search' class='btn btn-primary btn-block btn-lg'>Browse Classes</a></div>");
    // swap the course select with the course search when search button is clicked
    $('#course_search').click( function () {
        $('.col-xs-8 > div:nth-child(2)').fadeOut(400, function () {
        $('#course_search_form').fadeIn(500).removeClass('hidden');
        });
    });

	// convert browse file button to BS3 button
	// $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
        
 //        var input = $(this).parents('.input-group').find(':text'),
 //            log = numFiles > 1 ? numFiles + ' files selected' : label;
        
 //        if( input.length ) {
 //            input.val(log);
 //        } else {
 //            if( log ) alert(log);
 //        }     
 //    });
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
                        min: 0,
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
    
	window.autocomplete = new Autocomplete({
		form_selector: '.autocomplete',
		minimum_length: 1,
	});
	window.autocomplete.setup();
});

var Autocomplete = function(options) {
	this.form_selector = options.form_selector;
	this.url = options.url || window.location.pathname;
	this.delay = parseInt(options.delay || 300);
	this.minimum_length = parseInt(options.minimum_length || 3);
	this.form_elem = null;
	this.query_box = null;
};

Autocomplete.prototype.setup = function() {
	var self = this;

	this.form_elem = $(this.form_selector);
	console.log(this.form_elem);
	this.query_box = this.form_elem.find('input[name=course]');
	console.log(this.query_box);

	// Watch the input box.
	this.query_box.on('keyup', function() {
		var query = self.query_box.val();

		if(query.length < self.minimum_length) {
			return false;
		}
		self.fetch(query);
	});

	// On selecting a result, populate the search field.
	this.form_elem.on('click', '.ac-result', function(ev) {
		self.query_box.val($(this).text());
		$('.ac-results').remove();
		return false;
	});
};

Autocomplete.prototype.fetch = function(query) {
	var self = this;

	$.ajax({
		url: this.url,
		data: {
			'q': query,
		},
		success: function(data) {
			self.show_results(data);
		}
	});
};

Autocomplete.prototype.show_results = function(data) {
	// Remove any existing results.
	$('.ac-results').remove();

	var results = data.results || [];
	var results_wrapper = $('<div class="ac-results"></div>');
	var base_elem = $('<div class="result-wrapper"><a href="#" class="ac-result"></a></div>');

	if(results.length > 0) {
		for(var res_offset in results) {
			var elem = base_elem.clone();
			// Don't use .html(...) here, as you open yourself to XSS.
			// Really, you should use some form of templating.
			elem.find('.ac-result').text(results[res_offset]);
			results_wrapper.append(elem);
		}
	}
	else {
		var elemn = base_elem.clone();
		elemn.text("No results found.");
		results_wrapper.append(elemn);
	}

	this.query_box.after(results_wrapper);
};

// provide feedback on browse file button
// $(document).on('change', '.btn-file :file', function() {
//   var input = $(this),
//       numFiles = input.get(0).files ? input.get(0).files.length : 1,
//       label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
//   input.trigger('fileselect', [numFiles, label]);
// });
