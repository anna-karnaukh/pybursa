from django.views.generic import TemplateView
from views import ContactView

from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
