$(function(){
	// http or https needs to match the site requesting this resource
	ZeroClipboard.config( { swfPath: "http://ajax.cdnjs.com/ajax/libs/zeroclipboard/2.1.5/ZeroClipboard.swf" } );
	var client = new ZeroClipboard(document.getElementById("copy-button") );

	// ajax stuff
	var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	// csrf token stuff
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	/*
	 * posting a review 
	 */
	// hide the radio buttons
	 $("#vote input[type='radio']").addClass("hidden"); 
	// indicate thumbs up selection
	$("label.radio-inline .fa-thumbs-up").click(function () {
		$(this).addClass('fa-2x animated tada');
		$("label.radio-inline .fa-thumbs-down").removeClass('fa-2x animated tada');
    });
    // indicate thumbs down selection 
	$("label.radio-inline .fa-thumbs-down").click(function () {
		$(this).addClass('fa-2x animated tada');
		$("label.radio-inline .fa-thumbs-up").removeClass('fa-2x animated tada');
    });

	// when the user clicks on the review link, send ajax request
	var $submit_review = $('#submit-review');
	$submit_review.click(function() {
		$vote = $('form input[type=radio]:checked');
		$review = $('#review-comment');
		// document pk is stored in the link itself with html5 data-* attribute
		var pk = $(this).data('document');
		var messages = [];
		$.ajax({
			url: '/documents/review/',
			type: 'POST',
			data: {
				'document': pk,
				'review': $review.val(),
				'vote': $vote.val(),
			},
		})
		// success
		.done(function(data) {
			messages = data.messages;
			$('#rate_document').modal('hide');
		})
		.fail(function(data) {
			messages = data.responseJSON.messages;
		})
		.always(function() {
			// reguardless of success or failure, show messages to user
            $.each(messages, function (i, item) {
                addMessage(item.message, item.extra_tags);
            });
		});
		return false;
	});
	//Rating Review form validator
	$('#review').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            reviewRating: {
                validators: {
                    notEmpty: {
                        message: 'A rating selection is required'
                    }
                }
            },
            reviewComment: {
                validators: {
                    notEmpty: {
                        message: 'Please select a thumb rating and leave a review.'
                    },
                    stringLength: {
                        min: 4,
                        message: 'A review should be at least 4 charecters long!'
                    }
                }
            }
        }
    });
});

function addMessage(text, extra_tags) {
    var message = $(
		'<div class="alert alert-' + extra_tags + ' alert-dismissible" role="alert">' +
			'<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+
			'<ul class="messages">'+
				'<li class="' + extra_tags + '">' + text + '</li>'+
			'</ul>'+
		'</div>');
    $(".django-messages").append(message);
}
