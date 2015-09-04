/*
 * This is for things that should happen site wide
 */


$(function() {

    // make popovers stay when hovered over or when triggered element is hovered over

    $(".pop-stay").popover({ trigger: "manual" , html: true, animation:false})
    .on("mouseenter", function () {
        var _this = this;
        $(this).popover("show");
        $(".popover").on("mouseleave", function () {
            $(_this).popover('hide');
        });
    }).on("mouseleave", function () {
        var _this = this;
        setTimeout(function () {
            if (!$(".popover:hover").length) {
                $(_this).popover("hide");
            }
        }, 300);
    });

    // choose a random img and set it as backgrounf each day
    var now = new Date();
    var fullDaysSinceEpoch = Math.floor(now/8.64e7);
    var rand = Math.floor((Math.random() * MAX_BG_IMAGES) + 1);
    var current_pic;
    
    if(typeof(Storage) !== "undefined") {

        current_pic = localStorage.current_pic || rand;

        if (localStorage.last_day) {
            if (localStorage.last_day != fullDaysSinceEpoch) {
                localStorage.last_day = fullDaysSinceEpoch;
                current_pic = rand;
            }
        } else {
            localStorage.last_day = fullDaysSinceEpoch;
            current_pic = rand;
        }

        localStorage.current_pic = current_pic;

    } else {
        //TODO: we might make a javascript session here, it will take some time
         current_pic = rand;
    }

    //document.body.style.backgroundImage = "url('/static/landing/img/bg-" + current_pic + ".jpg')";
    $('#bg').css("background-image","url('/static/lib/img/bgimages/bg-" + current_pic + ".jpeg')");


    // add auto drop down functionality of drop downs
    $(".drop").hover(
        function() {
            $('.dropdown-menu', this).stop( true, true ).slideDown("fast");
            $(this).toggleClass('open');
            $('.tooltip').hide();
        },
        function() {
            $('.dropdown-menu', this).stop( true, true ).slideUp("fast");
            $(this).toggleClass('open');
            $('.tooltip').hide();
        }
    );

    //detect window size for nav dropdown
    // $(window).on('resize', function() {
    //      if ($(window).width() > 768) {

    //      // make dropdown link direct to profile page when clicked
    //      $('.user-dropdown-toggle').click(function() {
    //          var location = $(this).attr('href');
    //          window.location.href = location;
    //          return false;
    //      });
    //      }
    // });

    // if ($(window).width() > 768) {

    //     // make dropdown link direct to profile page when clicked
    //      $('.user-dropdown-toggle').click(function() {
    //          var location = $(this).attr('href');
    //          window.location.href = location;
    //          return false;
    //      });
    // }


     //test data for typeahead in the search bar
     //Commented out because it broke things on the calendar page
    //$('#mchp-search').typeahead({
        //source: ['CSC 420','ECON 200','ECON 300','ACCT 210','ACCT 300','MGMT 210','CSC 386','MGMT 300','MKTG 361']
    //});

    // style django error messages to mimic BS3
    var html = [],
        $list = $('.errorlist');

    html.push('<div class="errorlist">');
        $list.find('li').each(function() {
        html.push('<p class="text-danger small">' + $(this).text() + '</p>');
        });
    html.push('</div>');
    $list.replaceWith(html.join(''));

    /* messages */
    $messages = $('.django-messages');
    var messageDelay = 5000;
    // fade messages that were added on page load
    $messages.children('div').delay(messageDelay).addClass('animated bounceInRight').fadeOut(500, function(){
        $(this).remove();
    });

    /* When messages are appended dynamically, they should fade out too */
    // create an observer instance
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            var $nodes = $(mutation.addedNodes);
            $nodes.delay(messageDelay).addClass('animated bounceInRight').fadeOut(500, function(){
                $(this).remove();
            });
        });
    });
    // configuration of the observer:
    var config = { attributes: true, childList: true, characterData: true };
    // pass in the target node, as well as the observer options
    observer.observe($messages.get(0), config);

    /* custom scroll bar */
    // can be applied to any div
    $('.scrolls').enscroll({
        showOnHover: false,
        verticalTrackClass: 'track3',
        verticalHandleClass: 'handle3',
        scrollIncrement: 50,
    });

    // initiates tooltips using data toggle selector
    $('[data-toggle="tooltip"]').tooltip({
        container: 'body'
    });
    // initiates popovers using data toggle selector
    $('[data-toggle="popover"]').popover({
        container: 'body',
        trigger: 'hover'
    });

    // hover opacity for score bar
    $('.score-bar').on( "mouseenter", function () {
        $(this).css({'transition':'opacity .5s ease 0s', 'opacity':'1'});
    });
    $('.score-bar').on( "mouseleave", function () {
        $(this).css({'transition':'opacity .5s ease 0s', 'opacity':'.5'} );
    });
    //Score bar double click
    $('.score-bar').on( "dblclick", function () {
        // $('.score-breakdown').toggleClass('hidden').toggleClass('animated slideInRight');
        $('#score_1').toggleClass('hidden').toggleClass('animated slideInLeft');
        $('#score_2').toggleClass('hidden').toggleClass('animated slideInRight');
        $('#score_3').toggleClass('hidden').toggleClass('animated slideInRight');
        $('#level_score').removeClass('hidden').toggleClass('animated slideInLeft');
    });
    // score bar entrance on page load
    $('#score_1').css({'width':'35%', 'transition':'width 1.5s ease 0s'});
    $('#score_2').css({'width':'55%', 'transition':'width 2s ease 0s'});
    $('#score_3').css({'width':'10%', 'transition':'width 1s ease 0s'});


    //trigger user popover on hover and stay
    $(".user-popover").popover ({
        trigger: "manual",
        html: true,
        content: function() {
            return $('#userPopoverContent').html();
        },
        container: 'body',
    })
    .on("mouseenter", function () {
        var _this = this;
        $(this).popover("show");
        $(".popover").on("mouseleave", function () {
            $(_this).popover('hide');
        });
    })
    .on("mouseleave", function () {
        var _this = this;
        setTimeout(function () {
            if (!$(".popover:hover").length) {
                $(_this).popover("hide");
            }
        }, 100);
    });
    // won't work w/o the validator, its not needed on every page anyway
    // really this should only be called on pages that we know have a
    // #email-signup form TODO
    if($.bootstrapValidator) {
        loginModal();
    }

    // mark notifications read
    $('.sidebar-brand').on('mouseover', function() {
        mark_all_read();
        $('#notification-count').text('0');
        $('#notification-count').removeClass('unread-notification');
    });

    // for toggleing one time events
    $('.one-time-event').on('click', function  () {
        toggle_flag($(this).data('event'));
    });
    $('.one-time-alert').on('close.bs.alert', function  () {
        toggle_flag($(this).data('event'));
    });
    set_username();

    // open chat when this class is clicked
    $('.open-chat').on('click', function() {
        FHChat.transitionTo('maximized');
    });
});

var MCHP_USERNAME = '';
var set_username = function(username) {
    MCHP_USERNAME = $('.mchp-username').text();
};

var loginModal = function () {
    // show email sign up input when clicked
    $('#show-signup').on('click', function () {
        $('#login-options').fadeOut(250, function () {
            $('#email-signup').fadeIn(500).removeClass('hidden');
        });
    });

    //validate signup form
    $('#email-signup').bootstrapValidator({
        message: 'This value is not valid',
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
};

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

var toggle_flag = function(id) {
    $.ajax({
        url: '/profile/toggle-flag/',
        type: 'POST',
        data: {'event': id},
    });
};

var marked = false;
var mark_all_read = function() {
    if (!marked) {
        $.ajax({
            url: '/notification/mark-all/',
            type: 'POST',
        });
        marked = !marked;
    }
};
