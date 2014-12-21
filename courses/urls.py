from django.conf.urls import patterns, include, url
from courses.views import courses_list, courses_item, course_edit, course_add, course_delete


urlpatterns = patterns('',
    url(r'^$', courses_list, name='courses'),
    url(r'^(?P<course_id>\d+)/$', courses_item, name='course'),
    url(r'^(?P<course_id>\d+)/edit/$', course_edit, name="edit"),
    url(r'^add/$', course_add, name='add'),
    url(r'^(?P<course_id>\d+)/delete/$', course_delete, name="delete"),
)
