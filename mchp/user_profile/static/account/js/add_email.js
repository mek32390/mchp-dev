$(function() {
	// var message = "{% trans 'Do you really want to remove the selected e-mail address?' %}";
	// var actions = document.getElementsByName('action_remove');
	// if (actions.length) {
	//   actions[0].addEventListener("click", function(e) {
	//     if (! confirm(message)) {
	//       e.preventDefault();
	//     }
	//   });
	// },

	//show add email form on click
	$('#showEmailForm').on('click', function () {
	$('#addNewEmail').fadeIn(250).toggleClass('hidden');
	});

	$("#id_email").wrap( $( "<div class='form-group'><div class='input-group input-group-lg'></div></div>" ) );
	$("#id_email").before( "<span class='input-group-addon'><i class='fa fa-envelope fa-fw'></i></span>" );
	$("#id_email").addClass("form-control");
	$('#id_email').attr('placeholder','Enter .edu e-mail');

    // BS Validator 
    $('.add_email').bootstrapValidator({
        fields: {
            id_email: {
                trigger: 'blur',
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

	// hide unwanted labels
	$('label[for="id_email"]').hide();

	  // style error message to BS Validator
	  var html = [], $list = $('.errorlist');

	  html.push('<div class="errorlist">');
	  $list.find('li').each(function() {
	    html.push('<p class="text-danger small">' + $(this).text() + '</p>');
	});
	html.push('</div>');
	$list.replaceWith(html.join(''));
});