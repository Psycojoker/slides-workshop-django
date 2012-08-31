from django.conf.urls import patterns, include, url
from django.shortcuts import render
from models import Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def hello(request):
    return render(request, "hello.html", {"posts": Post.objects.all()})

urlpatterns = patterns('',
    # Examples:
    url(r'^$', hello, name='home'),
    # url(r'^blog_1/', include('blog_1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
