from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
    data = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': data
    }
    return HttpResponse(template.render(context, request))

def hello(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())