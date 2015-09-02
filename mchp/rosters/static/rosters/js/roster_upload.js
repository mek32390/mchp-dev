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

    function update_classname(){
        var selectedCourse = $('#id_course').find('option:selected').text();
        $('.selected-classname').text(selectedCourse);
        $('#id_course_name').val(selectedCourse);
    }
    update_classname();

    // initialize date picker
    $('.event-date').datepicker({
        startView: 1,
        multidate: false,
        autoclose: true,
        todayHighlight: false
    });
});