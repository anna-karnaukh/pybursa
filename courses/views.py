from django import forms 
from courses.models import Course
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


class CourseCreate(CreateView):
    model = Course
    template_name = "courses/edit.html"
    success_url = "/courses"


class CourseDelete(DeleteView):
    model = Course
    template_name = "courses/edit.html"
    success_url = "/courses"
    