function form_submit(param, action) {
    var form = $(param).parent().parent().parent();
    form.find('#hidden_roster_action').val(action);
    form.submit();
}