$(function() {
    $('.flip-container').on('mouseenter', function () {
        $('#instruction-text').addClass('fadeOutDown').toggleClass('delayed-5');
    });

    // change notif indicator when clicked
    $('#toggle-notifications').on('click', function () {
        $('#notification-count').css("background-color", "#777");
    });

    // BS Validator 
    $('#emailForm').bootstrapValidator({
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
                        message: 'Only .EDU emails allowed'
                    }
                }
            }
        }
    });
});
