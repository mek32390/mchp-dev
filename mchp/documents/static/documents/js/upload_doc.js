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
    var selected_course_name = $('#document_course').find('option:selected').text();
    var selected_course_id = $('#document_course').val();

    if (parseInt($("#document_type").val()) === SYLLABUS) {
        $("#id_title").val("Syllabus for course " + selected_course_name);
        $("#id_description").val("Syllabus for course " + selected_course_name);
    }

    $('.selected-classname').text(selected_course_name);
    $('#document_course_name').val(selected_course_name);
}

$(document).ready(function () {

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
});


$(document).on('change', '.btn-file :file', function () {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
});