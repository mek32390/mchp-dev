$(function() {

    // $('#homepage-example').on('mouseenter', function () {
    //     $('#instruction-text').addClass('animated fadeOutDown');
    // });

    // change notif indicator when clicked

    var MAX_PICS = 10; //TODO: move this to settings?
    var now = new Date();
    var fullDaysSinceEpoch = Math.floor(now/8.64e7);
    var rand = Math.floor((Math.random() * MAX_PICS) + 1);
     if(typeof(Storage) !== "undefined") {
        if (localStorage.rand) {
            // do nothing
        } else {
            localStorage.rand = Math.floor((Math.random() * MAX_PICS) + 1);
        }
        rand = localStorage.rand;
    } else {
        //TODO: we might make a javascript session here, it will take some time
    }
    current_pic = fullDaysSinceEpoch % rand;

    document.body.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/9/9c/Merops_bullockoides_1_Luc_Viatour.jpg')";


    $('#toggle-notifications').on('click', function () {
        $('#notification-count').css("background-color", "#777");
    });

    //toggle news categories section on click
    $('#edit-sections').on('click', function () {
        $('.flip-holder').toggleClass("flip");
    });

    //scrollspy news section 
    $("#news-scroll").scrollspy({
        target: "#news-navbar"
    });

    //set height of pulse and stories sections
    $('.pulse-con').css('max-height',$(window).height() - 100);
    $('#news-scroll').css('max-height',$(window).height() - 100);

    // set var for news section nav link click adjustment
    var offset = 1000;

    $('#news-navbar .nav li a').click(function (event) {
        event.preventDefault();

        var $link = $(this);
        var setting = $link.data('setting');

        $('#news-'+setting).get(0).scrollIntoView();
        scrollBy(0, -offset);

        $('.news-list-item').removeClass('active');
        $link.parents('li').addClass('active');

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
