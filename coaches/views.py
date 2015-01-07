from django import forms
from coaches.models import Coach
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import logging
logger = logging.getLogger(__name__)


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
    def form_valid(self, form):
        coach = form.save()
        logger.info('Coach with id %s changed' % coach.id)
        return super(CoachUpdate, self).form_valid(form)


class CoachCreate(CreateView):
    model = Coach
    template_name = "coaches/edit.html"
    success_url = "/coaches"
    def form_valid(self, form):
        coach = form.save()
        logger.info('New Coach created')
        return super(CoachCreate, self).form_valid(form)


class CoachDelete(DeleteView):
    model = Coach
    template_name = "coaches/edit.html"
    success_url = "/coaches"
