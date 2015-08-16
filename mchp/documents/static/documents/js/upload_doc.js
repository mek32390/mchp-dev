/*
 * upload_doc.js
 * 
 * This file is for the custom browse file feature
 */

$(function() {

	// convert select to nice input
	$("#id_course").addClass("form-control");
	// clear the value amount in the price field
	$("#id_price").attr("value","");
	// convert default browse file to nice input
	$("#id_document").wrap("<div class='input-lg form-control'></div>").addClass("btn");
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
                    }
                }
            },
			event: {
				validators: {
					callback: {
						callback: function(value) {
							if (parseInt($("#document_type").val()) === SYLLABUS) {
								return true;
							}

							if (!$('#hidden_course').val) {
								return {
									valid: false,
									message: "Select a course before selecting an event."
								}
							}

							return true;
						}
					}
				}
			},
            price: {
                validators: {
					callback: {
						message: "Please set this selling price of this document'",
						callback: function (value, validator, $field) {
							// Conditional validation based on document type
							if (parseInt($("#document_type").val()) === SYLLABUS) {
								return true;
            				}

							value = parseInt(value);

							if (!value) {
								return {
									valid: false,
									message: "Please set this selling price of this document"
								};
							}

							if (value < 0 || value > 1000000000) {
								return {
									valid: false,
									message: "The price must be between 0 and 1 billion!'"
								};
							}

							return true;
						}
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
	}).on('success.form.bv', function(e) {
		$('.loading').removeClass('hidden');
	});

	window.autocomplete = new Autocomplete({
		query_selector: "#id_course",
		minimum_length: 1,
		selected_callback: function(id) {
			var hidden = $('#hidden_course');
			hidden.val(id);
		},
		fetch: function(query) {
			var self = this;
			$.ajax({
				url: this.url,
				data: {
					'q': query
				},
				dataType: 'json',
				success: function(data) {
					var results = JSON.parse(data) || [];
					self.show_results(results);
				}
			});
		},
		row_display: function(result) {
			return result.fields.dept + " " + result.fields.course_number + " with Instructor " + result.fields.professor;
		},
		divider_title: "More courses",
	});
	window.autocomplete.setup();

	window.events_autocomplete = new Autocomplete({
		query_selector: "#id_event",
		minimum_length: 0,
		selected_callback: function(pk) {
			var hidden = $('#hidden_event');
			hidden.val(pk);
		},
		fetch: function(query) {
			var self = this;
			$.ajax({
				url: '/school/course/events/',
				data: {
					'course_id': $("#hidden_course").val(),
					'query': query
				},
				dataType: 'json',
				success: function(data) {
					var results = data.events;
					self.show_results(results);
				}
			});
		},
		row_display: function(result) {
			return result.title;
		}
	});
	window.events_autocomplete.setup();

	var STUDY_GUIDE = 0;
	var SYLLABUS = 1;

	var document_type_changed = function() {
		if (parseInt($("#document_type").val()) === SYLLABUS) {
			$("#document_price").hide();
		} else {
			$("#document_price").show();
		}
	};
	document_type_changed();
	$("#document_type").change(document_type_changed);
});

var Autocomplete = function(options) {
	this.query_selector = options.query_selector;
	this.url = options.url || window.location.pathname;
	this.delay = parseInt(options.delay || 300);
	this.minimum_length = parseInt(options.minimum_length);
	this.form_elem = null;
	this.query_box = null;

	this.selected_callback = options.selected_callback;
	this.fetch = options.fetch;
	this.row_display = options.row_display;
	this.divider_title = options.divider_title;
};

Autocomplete.prototype.setup = function() {
	var self = this;

	this.query_box = $(this.query_selector);
	// rename input field
	self.query_box.name = "display";
	self.dropdown = this.query_box.parent()
	self.drop = this.query_box.parent().find('#ac-dropdown');

	// Watch the input box.
	this.query_box.on('keyup', function() {
		self.dropdown.attr('class', 'dropdown open');

		var query = self.query_box.val();

		if(query.length < self.minimum_length) {
			// remove the old search results
			self.drop.find('.divider').remove();
			self.drop.find('.dropdown-header-added').remove();
			self.drop.find('.search-results').remove();
			return false;
		}
		self.fetch(query);
	});

	// On selecting a result, populate the search field.
	self.drop.click(function(what){
		// get the li element
		var $link = $(what.target).parent();

		// take off whitespace
		var display = $link.text().trim();
		self.query_box.val(display);

		// add the data-course to the hidden field
		self.selected_callback($link.data('id'));
	});
	
};

Autocomplete.prototype.show_results = function(results) {
	var self = this;
	// remove the old search results
	self.drop.find('.divider').remove();
	self.drop.find('.dropdown-header-added').remove();
	self.drop.find('.search-results').remove();

	// a new line for a class
	var $base_result_elem = $('<li class="search-results"><a href="#" class="ac-link"><i class="fa fa-fw fa-plus-circle text-success"></i> </a></li>');
	// if there are results, add a divider to divide them from enrolled classes
	if (results.length > 0 && self.divider_title) {
		$divider = $('<li class=divider></li><li role="presentation" class="dropdown-header dropdown-header-added">' + self.divider_title + '</li>');
		self.drop.append($divider);
	}
	// add a new li for each result
	$.each(results, function(i, result){
		var $result_elem = $base_result_elem.clone();
		var display = self.row_display(result);
		$result_elem.children('a').append(display);
		$result_elem.data('id', result.id);
		self.drop.append($result_elem);
	});
};
