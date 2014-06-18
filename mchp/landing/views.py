from django.shortcuts import render

from landing.models import PageHit

def index(request):
    agent = [request.META['HTTP_USER_AGENT']]
    #agent = PageHit.objects.all()[:5]
    context = {'user_agent': agent}
    return render(request, 'landing/index.html', context)
