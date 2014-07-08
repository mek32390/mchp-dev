$(function() {
    //ladda button
    Ladda.bind( '.ladda-button', { timeout: 1000 } );

    // BS validator
    $('#emailForm').bootstrapValidator({
        fields: {
            email: {
                trigger: 'blur',
                validators: {
                    notEmpty: {
                        message: 'Your college e-mail is required'
                    },
                    emailAddress: {
                        message: 'Please enter a valid e-mail address'
                    },
                    regexp: {
                        regexp: /(\.edu)$/,
                        message: 'You\'ll need a college e-mail to begin!'
                    }
                }
            }
        }
    });
});    
