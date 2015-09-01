/*
 * upload_roster.js
 *
 * This file is for the roster upload page
 */
"use strict";  // ECMAScript 5


$(document).on('change', '.btn-file :file', function () {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
});


$(document).ready(function () {
    $('.btn-file :file').on('fileselect', function (event, numFiles, label) {

        var input = $(this).parents('.input-group').find(':text'),
            log = numFiles > 1 ? numFiles + ' files selected' : label;

        if (input.length) {
            input.val(log);
        } else {
            if (log) $(".selected-file").html((log));
        }

    });

    $('#id_course').change(function () {
        update_classname();
    });

    $('#addEventRow').click(function () {
        add_exam_inputs();
    });

    function update_classname(){
        var selectedCourse = $('#id_course').find('option:selected').text();
        $('.selected-classname').text(selectedCourse);
        $('#id_course_name').val(selectedCourse);
    }
    update_classname();


    function add_exam_inputs() {
        var lastEventRow = $('.event-row').last();
        var lastId = parseInt(lastEventRow.attr('data-event-index'));
        var newEventRow = lastEventRow.clone();
        var newId = lastId + 1;
        // reset inputs & index
        newEventRow.attr('data-event-index', newId);
        newEventRow.find('.event-title').val('');
        newEventRow.find('.event-date').val('');
        // change placeholder + name
        newEventRow.find('.event-title').attr('placeholder', 'Exam ' + newId + ' Title');
        newEventRow.find('.event-date').attr('placeholder', 'Exam ' + newId + ' Date');

        newEventRow.find('.event-title').attr('name', 'form-' + newId + '-title');
        newEventRow.find('.event-date').attr('name', 'form-' + newId + '-date');

        newEventRow.find('.event-date').datepicker({
            startView: 1,
            multidate: false,
            autoclose: true,
            todayHighlight: false
        });
        newEventRow.appendTo(lastEventRow.parent());
        $('#id_form-TOTAL_FORMS').val(newId);
    }
});


$(document).ready(function () {

    // initialize date picker
    $('.event-date').datepicker({
        startView: 1,
        multidate: false,
        autoclose: true,
        todayHighlight: false
    });

    /*$.fn.editable.defaults.mode = 'inline';

     // Bootstrap Editable form fields

     // make the newly added fields editable
     $(".editField").editable({
     type: "email",
     highlight: "#000",
     showbuttons: false,
     anim: "med",
     onblur: 'submit'
     });

     $('.examSelect').editable({
     type: "select",
     showbuttons: false,
     anim: "med",
     onblur: 'submit',
     value: 1,
     source: [
     {value: 1, text: 'Exam 1'},
     {value: 2, text: 'Exam 2'},
     {value: 3, text: 'Exam 3'}
     ]
     });

     $('.rosterCode').editable({
     inputclass: "input-sm",
     showbuttons: false,
     anim: "med",
     onblur: 'submit',
     rows: 10
     });

     // When a user clicks to add a new instructor email, show them a new field

     $("#addInstructorEmail").click(function () {
     var nextListItem = $("#InstructorEmails").find("li.additionalInstr:hidden:first");
     nextListItem.removeClass("hidden");
     });
     */
});



