"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from django.views.generic import TemplateView
from rango import views
from registration.forms import RegistrationFormUniqueEmail


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmail
    def get_success_url(self, request, user):
        return '/rango/'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),

    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )












