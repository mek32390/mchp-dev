$(function() {

    // show email sign up form when clicked
    $('#show-signUp').on('click', function () {
        $('.facebookSignup').fadeOut(250, function () {
            $('.emailSignup').fadeIn(500);
            $('.email_reminder').fadeIn(500);
        });
    });
    // hide unwanted labels
    $('label').hide();
   
    // style error message to BS Validator
    var html = [],
        $list = $('.errorlist');

    html.push('<div class="errorlist">');
        $list.find('li').each(function() {
        html.push('<p class="text-danger small">' + $(this).text() + '</p>');
        });
    html.push('</div>');
    $list.replaceWith(html.join(''));
    
    // Convert form fields to BS Validator
    $("#id_first_name").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_first_name").before( "<span class='input-group-addon'><i class='fa fa-fw fa-user'></i></span>" );
    $("#id_first_name").addClass("form-control input-lg");

    $("#id_last_name").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_last_name").before( "<span class='input-group-addon'><i class='fa fa-fw fa-user'></i></span>" );
    $("#id_last_name").addClass("form-control input-lg");

    $("#id_username").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_username").before( "<span class='input-group-addon'><i class='fa fa-fw fa-user'></i></span>" );
    $("#id_username").addClass("form-control input-lg");

    $("#id_email").wrap( $( "<div class='form-group form-group-email'><div class='input-group'></div></div>" ) );
    $("#id_email").before( "<span class='input-group-addon'><i class='fa fa-fw fa-envelope'></i></span>" );
    $("#id_email").addClass("form-control input-lg");

    $("#id_password1").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_password1").before( "<span class='input-group-addon'><i class='fa fa-fw fa-lock'></i></span>" );
    $("#id_password1").addClass("form-control input-lg");

    $("#id_password2").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_password2").before( "<span class='input-group-addon'><i class='fa fa-fw fa-lock'></i></span>" );
    $("#id_password2").addClass("form-control input-lg");

    //validate signup form 
    $('#signup-form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            username: {
                validators: {
                    notEmpty: {
                        message: 'This field is required'
                    },
                    stringLength: {
                        min: 4,
                        message: 'Please make your username at least 4 characters long'
                    }
                }
            },
            email: {
                trigger: 'keyup',
                validators: {
                    notEmpty: {
                        message: 'This field is required'
                    },
                    emailAddress: {
                        message: 'Please enter a valid email address'
                    },
                    regexp: {
                        regexp: /(\.edu)$/,
                        message: 'Only .edu emails allowed'
                    }
                }
            },
            password1: {
                validators: {
                    notEmpty: {
                        message: 'This field is required'
                    },
                    stringLength: {
                        min: 8,
                        message: 'Please make your password at least 8 characters long'
                    },
                    identical: {
                        field: 'password2',
                        message: 'Your password must match the one below'
                    }
                }
            },
            password2: {
                validators: {
                    notEmpty: {
                        message: 'This field is required'
                    },
                    identical: {
                        field: 'password1',
                        message: 'Your password must match the one above'
                    }
                }
            }
        }
    });
});
