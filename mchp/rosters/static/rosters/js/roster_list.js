/*
/*
/* This is for roster-list functions
/*
*/

function form_submit(param, action) {
    var form = $(param).parents('form');
    form.find('#hidden_roster_action').val(action);
    form.find('#hidden_roster_action').val(action);
    form.submit();
}

