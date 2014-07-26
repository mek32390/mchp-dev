/*
 * calendar.js
 *
 * This file handles the functionality of the calendar page.
 */
$(document).ready(function() {
	// show calendar step three  when clicked
    $('.stepOneNext').on('click', function () {
    	$('#calStepOne').fadeOut(250, function () {
    		$('#calStepTwo').fadeIn(500);
    		$('#calStepTwo').removeClass("hidden");
    	});
	});
	// show calendar step three when clicked
    $('.stepTwoNext').on('click', function () {
	$('#calStepTwo').fadeOut(250, function () {
		$('#calStepThree').fadeIn(500);
		$('#calStepThree').removeClass("hidden");
		});
	});
	// switch to your cal list tab when clicked
	$('.stepThreeNext1').on('click', function () {
		$('.cal-intro').fadeOut(250, function () {
		$('#yourCalList').fadeIn(500);
		$('#yourCalList').removeClass("hidden");
		});
	});
	// switch to calendar list tab when clicked
	$('.stepThreeNext2').on('click', function () {
		$('.nav-tabs > .active').next('li').find('a').trigger('click');
		$('#col_1').addClass('col-sm-9', 1000, "easeOutQuart");
		$('#col_2').addClass('col-sm-3', 1000, "easeOutQuart");
		// $('.cal-intro').fadeOut(250);

	});
	// expand col_1 when cal list tab is clicked
	$('#calListTab').on('click', function () {
		$('#col_1').addClass('col-sm-9', 1000, "easeOutQuart");
		$('#col_1').removeClass('col-sm-3', 1000, "easeOutQuart");
		$('#col_2').addClass('col-sm-3', 1000, "easeOutQuart");
		$('#col_2').removeClass('col-sm-9', 1000, "easeOutQuart");
		$('#calendar').fullCalendar( 'changeView', 'agendaDay' )
	});
	// contract col_1 when your cal tab is clicked
	$('#yourCalTab').on('click', function () {
		$('#col_1').addClass('col-sm-3', 1000, "easeOutQuart");
		$('#col_2').switchClass('col-sm-3','col-sm-9', 1000, "easeOutQuart");
		$('#calendar').fullCalendar( 'changeView', 'month' )
	});
	
	// fullcalendar
	$('#calendar').fullCalendar({
		header: false,
    	weekMode: 'liquid',

    	//trigger add event pop-up on click and stay
        dayClick: function(date, jsEvent, view) {

		$(this).popover({
            html: true,
            placement: 'top',
            title: function() {
                return $("#popover-head").html();
            },
            content: function() {
                return $("#popover-content").html();
            }
        });
		$(this).popover('show');


		// $().popover ({ 
		// 	trigger: "manual",
		// 	html: true,
		// 	content : '<div class="text-center" style="width:200px;"><img class="img-circle img-thumbnail" src="https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfp1/t1.0-1/p160x160/1948074_10151938632961930_1503647379_n.jpg" width="120px"/><h5 style="margin-bottom:0px;">Mitch Kessler</h5><small style="margin-bottom:0px;">@mitchellias</small><h5><small>20 friends and 3 classes in common</small></h5><hr><small><div class="progress" style="margin-bottom:;"><a href="#" class="progress-bar progress-bar-success" style="width:20%;"></a><a href="#" class="progress-bar progress-bar-primary" style="width:20%;"></a><a href="#" class="progress-bar progress-bar-info" style="width:60%;" ></a></div></small></div>'
		// 	$(this).popover('show');
		// })


	 //    .on("mouseenter", function () {
	 //        var _this = this;
	 //        $(this).popover("show");
	 //        $(".popover").on("mouseleave", function () {
	 //            $(_this).popover('hide');
	 //        });
	 //    })
	 //    .on("mouseleave", function () {
	 //        var _this = this;
	 //        setTimeout(function () {
	 //            if (!$(".popover:hover").length) {
	 //                $(_this).popover("hide")
	 //            }
	 //        }, 100);
	 //    });

        // change the day's background color just for fun
        $(this).css('background-color', 'red');

    }
    });

	//	display date above calendar, could not set as var  
	$('.cal-date').html(function () {
		var view = $('#calendar').fullCalendar('getView');
		return view.title;
	});

	// create custom header buttons for cal
	$('.cal-today-button').click(function() {
    	$('#calendar').fullCalendar('today');
	});
	$('.cal-prev-button').click(function() {
    	$('#calendar').fullCalendar('prev');
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
 
	});
	$('.cal-next-button').click(function() {
    	$('#calendar').fullCalendar('next');
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});

	});
	$('.cal-month-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'month' );
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});
	$('.cal-agendaWeek-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'agendaWeek' );
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});
	$('.cal-agendaDay-button').click(function() {
    	$('#calendar').fullCalendar( 'changeView', 'agendaDay' );
    	//resort to messy function from above for now
    	$('.cal-date').html(function () {
			var view = $('#calendar').fullCalendar('getView');
			return view.title;
		});
	});
		
});
