$(document).ready(function() {
    $('.emailSignup').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        submitHandler: function(validator, form, submitButton) {
            $.post(form.attr('action'), form.serialize(), function(result) {
                // The result is a JSON formatted by your back-end
                // I assume the format is as following:
                //  {
                //      valid: true,          // false if the account is not found
                //      username: 'Username', // null if the account is not found
                //  }
                if (result.valid == true || result.valid == 'true') {
                    // You can reload the current location
                    window.location.reload();

                    // Or use Javascript to update your page, such as showing the account name
                    // $('#welcome').html('Hello ' + result.username);
                } else {
                    // The account is not found
                    // Show the errors
                    $('#errors').html('The account is not found').removeClass('hide');

                    // Enable the submit buttons
                    $('#loginForm').bootstrapValidator('disableSubmitButtons', false);
                }
            }, 'json');
        },
        fields: {
            first_name: {
                message: 'The first name is not valid',
                validators: {
                    notEmpty: {
                        message: 'Your first name is required and cannot be empty'
                    },
                    stringLength: {
                        min: 2,
                        max: 30,
                        message: 'Your first name must be more than 2 letters long'
                    },
                    regexp: {
                        regexp: /^[a-z]+$/i,
                        message: 'The first name can consist of letters only'
                    }
                }
            },
            last_name: {
                message: 'The last name is not valid',
                validators: {
                    notEmpty: {
                        message: 'Your last name is required and cannot be empty'
                    },
                    stringLength: {
                        min: 2,
                        max: 30,
                        message: 'The last name must be more than 2 and less than 30 letters long'
                    },
                    regexp: {
                        regexp: /^[a-z]+$/i,
                        message: 'The last name can consist of letters only'
                    }
                }
            },
            username: {
                message: 'The username is not valid',
                validators: {
                    notEmpty: {
                        message: 'Your username is required and cannot be empty'
                    },
                    stringLength: {
                        min: 8,
                        max: 32,
                        message: 'The username must be more than 8 and less than 32 characters long'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: 'Your username can only consist of alphabetical, number and underscore'
                    }
                }
            },
            password1: {
                validators: {
                    notEmpty: {
                        message: 'Your password is required and cannot be empty'
                    },
                    regexp: {
                        regexp: /^[A-Za-z0-9!@#$%^&*()_]{8,32}$/,
                        message: 'Password supports special characters and min length 8 max 32 characters.'
                    }
                }
            },
            password2: {
                validators: {
                    notEmpty: {
                        message: 'Your password is required and cannot be empty'
                    },
                    identical: {
                        field: 'password1',
                        message: 'The password must be the same as above'
                    }
                
                }
            },
        }
    });
});
