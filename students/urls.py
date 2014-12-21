from django.conf.urls import patterns, include, url
from students.views import students_list, students_item, student_edit, student_add, student_delete


urlpatterns = patterns('',
    url(r'^$', students_list, name='students'),
    url(r'^(?P<student_id>\d+)/$', students_item, name='student'),
    url(r'^(?P<student_id>\d+)/edit/$', student_edit, name="edit"),
    url(r'^add/$', student_add, name='add'),
    url(r'^(?P<student_id>\d+)/delete/$', student_delete, name="delete"),
)