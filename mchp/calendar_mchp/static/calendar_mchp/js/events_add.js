/*
 * events_add.js
 *
 * This file handles the functionality of the calendar events add page and bootstrap xeditable
 */
 $(function() {
    //display dropdown selection 
    $(".dropdown-menu li a").click(function(){
        //display the selected calendar in the button
        $(".btn:first-child").text($(this).text());
        $(".btn:first-child").val($(this).text()).append(" <span class='caret'></span>");
        //bring the course info and template into view once calendar is selected
        $('.course-info').fadeIn(500).removeClass('hidden');
        $('.event-template').fadeIn(700).removeClass('hidden');

    });

    //turn to inline mode
    $.fn.editable.defaults.mode = 'inline';
    //make editable field empty 
    $.fn.editable.defaults.emptytext = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';

    // initiate xeditable 
    $(".editField").editable({
        type: "text",
        showbuttons: false,
        anim: "fast"    

        //pk: 1,
        //url: '/post',   
    });
    // provide due date moments, we probably need times as well
    $('.due').editable({
        value: 1, 
        showbuttons: false,
        source: [
        {value: 1, text: 'In Class'},
        {value: 2, text: 'Before Class'},
        {value: 3, text: 'By Midnight'}
        ]
    });
    // tried to get it to switch to the next table data on "enter", but couldnt get it to go to the next row
    $('.editable').on('hidden', function(e, reason){
        if(reason === 'save' || reason === 'nochange') {
            var $next = $(this).closest('td').next().find('.editable');
            setTimeout(function() {
                $next.editable('show');
            }, 300);
        }
    });



});





