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

    // Change the student's name and classmates names on page refresh
    
    var names = ['Michelle','Nicole','Sam','Robert','Casey','Sarah','Michael','Jenny','Lindsey','Eric', 'Matt','Wyatt','Daniel','Kara','Rachel','Melissa','Luis','Pablo','Kevin','Jeremy','Carl','Lexi','Nicole','Adam','Alex','Claire','Sasha', 'Eric'];
    $(".studentName").html(names[Math.floor(Math.random() * names.length)]);
    $(".classmateName1").html(names[Math.floor(Math.random() * names.length)]);
    $(".classmateName2").html(names[Math.floor(Math.random() * names.length)]);

    // Change the greeting on page refresh
    
    var greetings = ['Hello,','Welcome back,','Good afternoon,','Goodmorning,','Hi there,','Hola,','Good to see you again,','Good evening,','Howdy,', 'Good day,'];

    $("#greeting").html(greetings[Math.floor(Math.random() * greetings.length)]);

    // Change the Course names on page refresh
    
    var courses = ['ECON 200','MKTG 361','RELI 100','MGMT 310','PHYS 600','CHEM 151','MUS 109','ENGL 101','MATH 100','MKTG 300','BUS 310','ENGL 330','RELI 160','ACCT 200','ACCT 210','MIS 111','MIS 373','MGMT 276'];

    $(".courseName1").html(courses[Math.floor(Math.random() * courses.length)]);
    $(".courseName2").html(courses[Math.floor(Math.random() * courses.length)]);
    $(".courseName3").html(courses[Math.floor(Math.random() * courses.length)]);
    $(".courseName4").html(courses[Math.floor(Math.random() * courses.length)]);
    $(".courseName5").html(courses[Math.floor(Math.random() * courses.length)]);


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