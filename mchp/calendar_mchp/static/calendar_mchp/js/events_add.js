/*
 * events_add.js
 *
 * This file handles the functionality of the calendar events add page and bootstrap xeditable
 */
 $(function() {
	 var activeCalendar = null;
	 //display dropdown selection 
	 $(".dropdown-menu li a").click(function(){
		 var pk = $(this).data('cal');
		 //display the selected calendar in the button
		 $(".btn:first-child").text($(this).text());
		 $(".btn:first-child").val($(this).text()).append(" <span class='caret'></span>");
		 //bring the course info and template into view once calendar is selected
		 $('.course-info').hide();
		 $('#course-info-'+pk).fadeIn(500).removeClass('hidden');
		 $('.event-template').fadeIn(700).removeClass('hidden');
		 activeCalendar = pk;
	 });

	 //turn to inline mode
	 $.fn.editable.defaults.mode = 'inline';
	 //make editable field empty 
	 var empty_text = '';
	 for(var i = 0 ; i < 40; i++) {
		 empty_text += '&nbsp;';
	 }
	 $.fn.editable.defaults.emptytext = empty_text;

	 // initiate xeditable 
	 $(".editField").editable({
		 type: "text",
		 showbuttons: false,
		 anim: "fast"    
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
