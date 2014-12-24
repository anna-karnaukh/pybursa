from django import forms
from coaches.models import Coach
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CoachModelForm(forms.ModelForm):
    error_css_class = 'errorList'
    class Meta:
        model = Coach


class CoachList(ListView):
    model = Coach
    template_name = "coaches/coaches.html"


class CoachDetail(DetailView):
    model = Coach
    template_name = "coaches/coach.html"


class CoachUpdate(UpdateView):
    model = Coach
    template_name = "coaches/edit.html"
    success_url = "/coaches"


class CoachCreate(CreateView):
    model = Coach
    template_name = "coaches/edit.html"
    success_url = "/coaches"


class CoachDelete(DeleteView):
    model = Coach
    template_name = "coaches/edit.html"
    success_url = "/coaches"
