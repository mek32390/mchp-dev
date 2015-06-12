from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from lib.decorators import school_required
from . import models


class RosterCreate(CreateView):
    template_name_suffix = '_create_form'
    model = models.Roster
    success_url = reverse_lazy('roster-upload')
    fields = ['course', 'code']

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.make_models()
        form.instance.created_by = self.request.user.student_user
        return super().form_valid(form)

    # @school_required
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
