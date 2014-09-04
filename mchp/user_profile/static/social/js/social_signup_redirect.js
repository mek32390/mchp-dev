$(function() {
    // hide unwanted labels
    $('label').hide();

    // this is to add the session stored email address, and hide that field
    $('.email_reminder').hide();
    hidden = $('input[name=saved_email]').attr('value');
    if(hidden !== ''){
        $('#id_email').hide();
        $('.form-group-email').hide();
        $('label[for=id_email]').hide();
        $('#id_email').attr('value', hidden);
    } else if(hidden === '') {
        // if there is no session email, this will show the e-mail input field
		$('.email_reminder').show();
        $('.email_reminder h4').html("Sign up with E-mail");
    }
	$form = ($('#signup_form'));
    var username = $('#id_first_name').attr('value') + $('#id_last_name').attr('value');
    console.log($('#id_firstname'));
    console.log(username);
	$('#id_username').val(username); 
	$('#id_email').text(hidden);
    // don't loop if the form doesn't validate
    if(document.referrer === document.URL) {
    } else {
		$form.submit();
	}
    
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

    //validate signup form 
    $('#signup_form').bootstrapValidator({
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
            }
        }
    });
});
