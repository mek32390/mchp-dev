/*
 * events_add.js
 *
 * This file handles the functionality of the calendar events add page and bootstrap xeditable
 */
$(function() {

	//turn to inline mode
	$.fn.editable.defaults.mode = 'inline';
	$.fn.editable.defaults.emptytext = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';

	//bs xeditable options
    $(".editField").editable({
	    type: "text",
	    showbuttons: false,
	    anim: "fast"    

	    //pk: 1,
	    //url: '/post',   
    });
    
    $('.due').editable({
        value: 1, 
        showbuttons: false,
        source: [
              {value: 1, text: 'In Class'},
              {value: 2, text: 'Before Class'},
              {value: 3, text: 'By Midnight'}
           ]
    });
    
    $('.editable').on('hidden', function(e, reason){
        if(reason === 'save' || reason === 'nochange') {
            var $next = $(this).closest('td').next().find('.editable');
            setTimeout(function() {
                    $next.editable('show');
                }, 300);
        }
   });

});




	
