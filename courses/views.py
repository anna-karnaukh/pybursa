from django import forms 
from courses.models import Course
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import logging
logger = logging.getLogger(__name__)


class CourseModelForm(forms.ModelForm):
    error_css_class = 'errorList'
    class Meta:
        model = Course


class CourseList(ListView):
    model = Course
    template_name = "courses/courses.html"


class CourseDetail(DetailView):
    model = Course
    template_name = "courses/course.html"


class CourseUpdate(UpdateView):
    model = Course
    template_name = "courses/edit.html"
    success_url = "/courses"
    def form_valid(self, form):
        course = form.save()
        logger.info('Course with id %s changed' % course.id)
        return super(CourseUpdate, self).form_valid(form)


class CourseCreate(CreateView):
    model = Course
    template_name = "courses/edit.html"
    success_url = "/courses"
    def form_valid(self, form):
        course = form.save()
        logger.info('New Course created')
        return super(CourseCreate, self).form_valid(form)


class CourseDelete(DeleteView):
    model = Course
    template_name = "courses/edit.html"
    success_url = "/courses"
