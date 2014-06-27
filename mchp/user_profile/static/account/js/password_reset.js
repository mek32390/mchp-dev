$(function() {
    $("#id_email").focus();
    $("#id_email").attr("placeholder", "Enter your .edu e-mail");
    $("label").hide();

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
    $("#id_email").wrap( $( "<div class='form-group'><div class='input-group'></div></div>" ) );
    $("#id_email").before( "<span class='input-group-addon'><i class='fa fa-envelope fa-fw'></i></span>" );
    $("#id_email").addClass("form-control input-lg");

    // BS Validator 
    $('.password_reset').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
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
            }
        }
    });
});
