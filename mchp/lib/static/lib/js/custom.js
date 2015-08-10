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


    // Change the background image on page refresh
    // These images are located in a folder
    
    var images = ['sheep.jpg','yacht.jpg','island.jpg','waterfall.jpg','watercup.jpg','plant.jpg','boathouse.jpg','path.jpg','nyskyline.jpg','forest.jpg', 'mountains.jpeg', 'greenhills.jpeg', 'waterfall.jpeg', 'plains.jpeg', 'flowers.jpeg', 'sunset.jpeg', 'cloud.jpeg', 'sunset_mountains.jpeg'];

    // #bg is the div that spans the entire page

    $('#bg')
        .css({'background-image': 'url(../home/assets/images/' + images[Math.floor(Math.random() * images.length)] + ')'
    });


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


    // FULLCALENDAR Options

    // Set custom header buttons 

    $('.cal-prev-button').click(function() {
        $('#calendar').fullCalendar('prev');
    });

    $('.cal-today-button').click(function() {
        $('#calendar').fullCalendar('today');
    });

    $('.cal-next-button').click(function() {
        $('#calendar').fullCalendar('next');
    });

    $('.cal-view-day').click(function() {
        $('#calendar').fullCalendar('changeView', 'agendaDay');
    });

    $('.cal-view-week').click(function() {
        $('#calendar').fullCalendar('changeView', 'agendaWeek');
    });

    $('.cal-view-month').click(function() {
        $('#calendar').fullCalendar('changeView', 'month');
    });

    //  custom date above calendar 
    $('.cal-date').html(function () {
        var view = $('#calendar').fullCalendar('getView');
        return view.title;
    });

    // change the title when the view changes
    $('.cal-button').click(function() {
        $('.cal-date').text(function () {
            var view = $('#calendar').fullCalendar('getView');
            return view.title;
        });
    });

    var date = new Date();
    var d = date.getDate();
    var m = date.getMonth();
    var y = date.getFullYear();
    
    /*  className colors
    
    className: default(transparent), important(red), chill(pink), success(green), info(blue)
    
    */      
    

    /* initialize the calendar
    -----------------------------------------------------------------*/
    
    var calendar =  $('#calendar').fullCalendar({
        header: false,
        editable: true,
        firstDay: 1, //  1(Monday) this can be changed to 0(Sunday) for the USA system
        selectable: true,
        defaultView: 'month',
        
        axisFormat: '',
        columnFormat: {
            month: '',    // Mon
            week: '', // Mon 7
            day: '',  // Monday 9/7
            agendaDay: ''
        },
        titleFormat: {
            month: '', // June 2015
            week: "", // Jun 22 — 28, 2015
            day: ''  // Jun 25, 2015
        },
        allDaySlot: false,
        selectHelper: true,
        select: function(start, end, allDay) {
            var title = prompt('Event Title:');
            if (title) {
                calendar.fullCalendar('renderEvent',
                    {
                        title: title,
                        start: start,
                        end: end,
                        allDay: allDay
                    },
                    true // make the event "stick"
                );
            }
            calendar.fullCalendar('unselect');
        },
        droppable: true, // this allows things to be dropped onto the calendar !!!
        drop: function(date, allDay) { // this function is called when something is dropped
        
            // retrieve the dropped element's stored Event Object
            var originalEventObject = $(this).data('eventObject');
            
            // we need to copy it, so that multiple events don't have a reference to the same object
            var copiedEventObject = $.extend({}, originalEventObject);
            
            // assign it the date that was reported
            copiedEventObject.start = date;
            copiedEventObject.allDay = allDay;
            
            // render the event on the calendar
            // the last `true` argument determines if the event "sticks" (http://arshaw.com/fullcalendar/docs/event_rendering/renderEvent/)
            $('#calendar').fullCalendar('renderEvent', copiedEventObject, true);
            
            // is the "remove after drop" checkbox checked?
            if ($('#drop-remove').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }
            
        },
        
        events: [
            {
                title: 'All Day Event',
                start: new Date(y, m, 1)
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: new Date(y, m, d-3, 16, 0),
                allDay: false,
                className: 'info'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: new Date(y, m, d+4, 16, 0),
                allDay: false,
                className: 'info'
            },
            {
                title: 'Meeting',
                start: new Date(y, m, d, 10, 30),
                allDay: false,
                className: 'important'
            },
            {
                title: 'Lunch',
                start: new Date(y, m, d, 12, 0),
                end: new Date(y, m, d, 14, 0),
                allDay: false,
                className: 'important'
            },
            {
                title: 'Birthday Party',
                start: new Date(y, m, d+1, 19, 0),
                end: new Date(y, m, d+1, 22, 30),
                allDay: false,
            },
            {
                title: 'Click for Google',
                start: new Date(y, m, 28),
                end: new Date(y, m, 29),
                url: 'http://google.com/',
                className: 'success'
            }
        ],          
    });

});