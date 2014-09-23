from django.shortcuts import render
from django.views.generic.edit import View


'''
url: /demo/
name: demo
'''
class DemoView(View):
    template_name = 'demo/demo.html'

    def get(self, request, *args, **kwargs):
        data = {
            'um': 'what',
        }
        return render(request, self.template_name, data)

demo = DemoView.as_view()
