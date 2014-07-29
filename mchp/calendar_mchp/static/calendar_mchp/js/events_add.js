/*
 * events_add.js
 *
 * This file handles the functionality of the calendar events add page and bootstrap xeditable
 */
$(function() {
    $(".dropdown-menu li a").click(function(){
    //display dropdown selection in the button
      $(".btn:first-child").text($(this).text());
      $(".btn:first-child").val($(this).text()).append(" <span class='caret'></span>");
      //fade in course info and the template on selection
      $('.course-info').fadeIn(500).removeClass('hidden');
      $('.event-template').fadeIn(700).removeClass('hidden');
    });

	//iniitiating bs xeditable
    $(".editField").editable({
       type: "text",
       showbuttons: false,
       anim: "fast"    
	    //pk: 1,
	    //url: '/post',   
    });
    // due date drop down- we probably need times in there too
    $('.due').editable({
        value: 1, 
        showbuttons: false,
        source: [
        {value: 1, text: 'In Class'},
        {value: 2, text: 'Before Class'},
        {value: 3, text: 'By Midnight'}
        ]
    });
    // make editable go to next field in row on enter, can't get it to go to the next row though
    $('.editable').on('hidden', function(e, reason){
        if(reason === 'save' || reason === 'nochange') {
            var $next = $(this).closest('td').next().find('.editable');
            setTimeout(function() {
                $next.editable('show');
            }, 300);
        }
    });
    //turn to inline mode
    $.fn.editable.defaults.mode = 'inline';
    //make empty text almost display as blank
    $.fn.editable.defaults.emptytext = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';

});





