from django.conf.urls import patterns, include, url
from coaches.views import (CoachList, CoachDetail, CoachUpdate, CoachCreate, CoachDelete)


urlpatterns = patterns('',
    url(r'^$', CoachList.as_view(), name='coaches'),
    url(r'^(?P<pk>\d+)/$', CoachDetail.as_view(), name='coach'),
    url(r'^(?P<pk>\d+)/edit/$', CoachUpdate.as_view(), name="edit"),
    url(r'^add/$', CoachCreate.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/delete/$', CoachDelete.as_view(), name="delete"),
)
