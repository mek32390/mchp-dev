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

    $('#upload_form').attr('action', '#'); // weird hacky fix to fix form action changing to data:,

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
        newEventRow.find('.event-title').attr('placeholder', 'Exam or Assignment Title');
        newEventRow.find('.event-date').attr('placeholder', 'Exam or Assignment Date');

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

    // initialize date picker
    $('.event-date').datepicker({
        startView: 1,
        multidate: false,
        autoclose: true,
        todayHighlight: false
    });

    $('#upload_form').on('success.form.bv', function (e) {
        $('.loading').removeClass('hidden');
    });
});
