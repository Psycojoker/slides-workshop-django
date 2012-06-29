from django.conf.urls import patterns, url
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

urlpatterns = patterns('',
    url(r'^$', hello, name='home'),
)
