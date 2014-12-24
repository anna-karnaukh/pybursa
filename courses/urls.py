from django.conf.urls import patterns, include, url
from courses.views import (CourseList, CourseDetail, CourseUpdate, CourseCreate, CourseDelete)


urlpatterns = patterns('',
    url(r'^$', CourseList.as_view(), name='courses'),
    url(r'^(?P<pk>\d+)/$', CourseDetail.as_view(), name='course'),
    url(r'^(?P<pk>\d+)/edit/$', CourseUpdate.as_view(), name="edit"),
    url(r'^add/$', CourseCreate.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/delete/$', CourseDelete.as_view(), name="delete"),
)
