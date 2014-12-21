from django.conf.urls import patterns, include, url
from coaches.views import coaches_list, coaches_item, coach_edit, coach_add, coach_delete


urlpatterns = patterns('',
    url(r'^$', coaches_list, name='coaches'),
    url(r'^(?P<coach_id>\d+)/$', coaches_item, name='coach'),
    url(r'^(?P<coach_id>\d+)/edit/$', coach_edit, name="edit"),
    url(r'^add/$', coach_add, name='add'),
    url(r'^(?P<coach_id>\d+)/delete/$', coach_delete, name="delete"),
)
