/*
/*
/* Custom js functions for the homepage
/*
*/

$(document).ready(function() {

    $(document).on('mouseenter', '.wrapperHolder', function () {
        $(this).find(".addNewWrapper").show();
    }).on('mouseleave', '.wrapperHolder', function () {
        $(this).find(".addNewWrapper").hide();
    });


    // To show the class tab in the classes section when the class link is clicked in the home section

    $("#course1Link").click(function() {
        $('.nav-pills a[href="#course1"]').tab('show');
    });
    $("#course2Link").click(function() {
        $('.nav-pills a[href="#course2"]').tab('show');
    });
    $("#course3Link").click(function() {
        $('.nav-pills a[href="#course3"]').tab('show');
    });
    $("#course4Link").click(function() {
        $('.nav-pills a[href="#course4"]').tab('show');
    });
    $("#course5Link").click(function() {
        $('.nav-pills a[href="#course5"]').tab('show');
    });

    // THE FOLLOWING ARE FOR TESTING PURPOSES

    // Change various aspects of the page each time the page loads for testing purposes

    // Change the greeting on page refresh
    
    var greetings = ['Hello,','Welcome back,','Hi there,','Hola,','Good to see you again,','Howdy,', 'Good day,'];

    $("#greeting").html(greetings[Math.floor(Math.random() * greetings.length)]);

    // Display current date and time on homepage

    // moment().format();

    var weekdayMonth = moment().format('dddd, MMMM'); // Friday, June
    $(".weekdayMonth").html(weekdayMonth);

    var numberDate = moment().format('D'); // 27
    $(".numberDate").html(numberDate);


    // Display date and time of event on event page

    var eventDate = moment([2015, 8, 29]).format('dddd, MMM Do, YYYY'); // Tuesday, September 29th, 2015
    $(".eventDate").html(eventDate);

    var eventDateFromNow = moment([2015, 8, 29]).fromNow();

    // var eventdate = moment([2007, 0, 29]).toNow();
    $(".eventDateFromNow").html(eventDateFromNow);


});