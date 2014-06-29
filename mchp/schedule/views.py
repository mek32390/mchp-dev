# from django.shortcuts import render
# from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from schedule.forms import CourseCreateForm

class CourseCreateView(FormView):
    template_name = 'schedule/course_create.html'
    form_class = CourseCreateForm
    #success_url = reverse('schedule/course_create')
    success_url = '/school/course/create/' 

    def form_valid(self, form):
        return super(CourseCreateView, self).form_valid(form)

    # def get(self, request):
    #     data = {
    #         'um': 'what',
    #         'k': {
    #             'asdf': 'fuck',
    #         }
    #     }
    #     return render(request, self.template_name, data)


    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(CourseCreateView, self).dispatch(*args, **kwargs)

course_create = CourseCreateView.as_view()

@verified_email_required
def course_remove(request):
    pass

@verified_email_required
def course_add(request):
    pass
