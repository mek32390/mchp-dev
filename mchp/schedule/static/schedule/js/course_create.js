$(document).ready( function() {
    // show college select form when clicked
    $('.show-college').on('click', function () {
        $('.display-college').fadeOut(250, function () {
            $('#college_select').fadeIn(500);
        });
    });

    // Create Class Form Validation
	$('#course_create').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        // Set default threshold for all fields. It is null by default
        threshold: 3,
        fields: {
            dept: {
                validators: {
                    notEmpty: {
                        message: 'The course code is required'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z]+$/i,
                        message: 'The course code can only consist of alphabetical characters'
                    },
                    stringLength: {
                        min: 3,
                        max: 6,
                        message: 'the course code should be between 3-6 characters'
                    }
                }
            },
            course_number: {
                validators: {
                    notEmpty: {
                        message: 'The course number is required'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'The course number can only consist of numbers. Disregard any letters attached to it.'
                    },
                    stringLength: {
                        min: 3,
                        max: 5,
                        message: 'the course number should be between 3-6 characters'
                    }
                }
            },
            professor: {
                validators: {
                    notEmpty: {
                        message: 'The course professor\'s last name is required'
                    },
                    regexp: {
                        regexp: /^[a-z]+$/i,
                        message: 'The professor\'s last name can consist of alphabetical characters only with no spaces'
                    },
                    stringLength: {
                        min: 2,
                        max: 20,
                        message: 'the professor\'s last name should be between 2-20 characters'
                    }
                }
            }
        }
    });
});
