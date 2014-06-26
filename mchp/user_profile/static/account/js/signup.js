$(function() {
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

    // Convert form to BS Validator
    $("#id_first_name").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_first_name").before( "<span class='input-group-addon glyphicon glyphicon-user'></span>" );
    $("#id_first_name").addClass("form-control input-lg");

    $("#id_last_name").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_last_name").before( "<span class='input-group-addon glyphicon glyphicon-user'></span>" );
    $("#id_last_name").addClass("form-control input-lg");

    $("#id_username").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_username").before( "<span class='input-group-addon glyphicon glyphicon-user'></span>" );
    $("#id_username").addClass("form-control input-lg");

    $("#id_password1").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_password1").before( "<span class='input-group-addon glyphicon glyphicon-lock'></span>" );
    $("#id_password1").addClass("form-control input-lg");

    $("#id_password2").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_password2").before( "<span class='input-group-addon glyphicon glyphicon-lock'></span>" );
    $("#id_password2").addClass("form-control input-lg");

    // BS Validator 
    $('#signup_form').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            username: {
                trigger: 'keyup',
                validators: {
                    notEmpty: {
                        message: 'This field is required'
                    },
                    stringLength: {
                        min: 4,
                        message: 'Your username or email must be more than 4 characters'
                    }
                }
            },
            password1: {
                trigger: 'keyup',
                validators: {
                    notEmpty: {
                        message: 'This field is required'
                    },
                    stringLength: {
                        min: 8,
                        message: 'Your password must be at least 8 characters'
                    },
                    identical: {
                        field: 'password2',
                        message: 'Your password must match the one below'
                    }
                }
            },
            password2: {
                trigger: 'keyup',
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
