var STUDY_GUIDE = 0;
var SYLLABUS = 1;

var study_guide_title, study_guide_description, study_guide_price


function update_title_numbering() {
    $('.upload-form .media:visible').each(function (i, media) { // for each visible title heading
        $(media).find('.media-object.pull-left').html(i + 1 + '.'); // compensate for 0-based array iterator
        i++;
    });
}

function document_type_changed() {
    console.log('type changed')
    if (parseInt($("#document_type").val()) === SYLLABUS) {

        study_guide_price = $('#id_price').val();
        $("#price_container").hide();
        $('#id_price').val(0);

        var selected_course = $('#document_course').val();

        $("#title_container").hide();
        study_guide_title = $("#id_title").val();

        $("#description_container").hide();
        study_guide_description = $("#id_description").val();

        $("#event_container").hide();
        study_guide_event = $("#id_event").val();

        update_classname();
    } else {
        $('#id_price').val(study_guide_price);
        $("#price_container").show();

        $("#id_title").val(study_guide_title);
        $("#title_container").show();

        $("#id_description").val(study_guide_description);
        $("#description_container").show();
    }

    $('.selected-typename').text($("#document_type :selected").text());


    update_title_numbering();
};

function update_classname() {
    console.log("class changed");
    var selected_course_name = $('#id_course').data('name');
    var selected_course_id = $('#hidden_course').val();

    if (parseInt($("#document_type").val()) === SYLLABUS) {
        $("#id_title").val("Syllabus for " + selected_course_name);
        $("#id_description").val("Syllabus for " + selected_course_name);
    }

    $('.selected-classname').text(selected_course_name);
    $('#document_course_name').val(selected_course_name);

    update_events(selected_course_id);
}

function update_events(selected_course_id) {
    $("#document_event").find('option').not(':first').remove();
    var events = student_course_events[selected_course_id];

    if (events) {
        for (var i=0; i<events.length; i++) {
            var event = events[i];
            $("#document_event").append(
                $("<option/>").attr("value", event.id).text(event.title + ' on ' + event.start)
            )
        }
    }
}

$(document).ready(function () {

    // convert select to nice input
	$("#id_course").addClass("form-control");

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
    }).on('success.form.bv', function (e) {
        $('.loading').removeClass('hidden');
    });

    $('.btn-file :file').on('fileselect', function (event, numFiles, label) {

        var input = $(this).parents('.input-group').find(':text'),
            log = numFiles > 1 ? numFiles + ' files selected' : label;

        if (input.length) {
            input.val(log);
        } else {
            if (log) $(".selected-file").html((log));
        }
    });

    $("#document_type").change(document_type_changed);
    $('#document_course').change(update_classname);

    document_type_changed();
    update_classname();

    window.autocomplete = new Autocomplete({
		form_selector: '.autocomplete',
		minimum_length: 1,
	});
	window.autocomplete.setup();
});


$(document).on('change', '.btn-file :file', function () {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
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
	this.query_box = $('#id_course');
	// rename input field
	self.query_box.name = "display";
	var $drop = $('#ac-dropdown');

	// Watch the input box.
	this.query_box.on('keyup', function() {
		$('#drop-li').attr('class', 'dropdown open');
        $hidden = $('#hidden_course');
		$hidden.val('');

		var query = self.query_box.val();

		if(query.length < self.minimum_length) {
			// remove the old search results
			$drop.find('.divider').remove();
			$drop.find('.dropdown-header-added').remove();
			$drop.find('.search-results').remove();
			return false;
		}
		self.fetch(query);
	});

	// On selecting a result, populate the search field.
	$drop.find('li.course').click(function(what){
		// get the li element
		var $link = $($(what.target).parents('li')[0]);

		// take off whitespace
		var display = $link.text().trim();
		self.query_box.val(display);
        self.query_box.data('name', $link.data('name'));


		// add the data-course to the hidden field
		var pk = $link.data('course');
		$hidden = $('#hidden_course');
		$hidden.val(pk);
        update_classname();
	});

};

Autocomplete.prototype.fetch = function(query) {
	var self = this;

	$.ajax({
		url: this.url,
		data: {
			'q': query,
		},
		dataType: 'json',
		success: function(data) {
			var results = JSON.parse(data) || [];
			self.show_results(results);
		}
	});
};

Autocomplete.prototype.show_results = function(results) {
	$drop = $('#ac-dropdown');
	// remove the old search results
	$drop.find('.divider').remove();
	$drop.find('.dropdown-header-added').remove();
	$drop.find('.search-results').remove();

	// a new line for a class
	var $base_result_elem = $('<li class="search-results"><a href="#" class="ac-link"><i class="fa fa-fw fa-plus"></i> </a></li>');
	// if there are results, add a divider to divide them from enrolled classes
	if (results.length > 0) {
		$divider = $('<li class=divider></li><li role="presentation" class="dropdown-header dropdown-header-added">More Courses</li>');
		$drop.append($divider);
	}
	// add a new li for each result
	$.each(results, function(i, result){
		var $result_elem = $base_result_elem.clone();
		var display = result.fields.dept + " " + result.fields.course_number + " with Instructor " + result.fields.professor;
		$result_elem.children('a').append(display);
		$result_elem.data('course', result.pk);
		$drop.append($result_elem);

        $drop.find('li').click(function(what){
		// get the li element
		var $link = $(what.target).parent();

		// take off whitespace
		var display = $link.text().trim();
		$('#id_course').val(display);
        $('#id_course').data('name', result.fields.dept + " " + result.fields.course_number);

		// add the data-course to the hidden field
		var pk = $link.data('course');
		$hidden = $('#hidden_course');
		$hidden.val(pk);
            update_classname();
	});

	});
};