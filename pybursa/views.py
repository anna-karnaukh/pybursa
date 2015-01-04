from django import forms
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _

from coaches.models import Coach
from students.models import Student


class ContactForm(forms.Form):
    theme = forms.CharField(label=_("Theme"))
    coach = forms.ModelChoiceField(queryset=Coach.objects.filter(coach_type='T'),
                                   widget=forms.RadioSelect,
                                   empty_label=None, label=_("Coach"))
    student = forms.ModelChoiceField(queryset=Student.objects.all(),
                                     widget=forms.RadioSelect,
                                     empty_label=None, label=_("Student"))
    text = forms.CharField(widget=forms.Textarea(), label=_("Text"))
    email = forms.EmailField(label=_("Email"))

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    
    def form_valid(self, form):
        coach = form.cleaned_data['coach']
        student = form.cleaned_data['student']
        theme = form.cleaned_data['theme']
        text = form.cleaned_data['text']
        email = form.cleaned_data['email']
        mail_body = render_to_string('mail.html', {'coach': coach,
                                                   'student': student,
                                                   'text': text})
        send_mail(theme, mail_body, email, ['to@example.com'],
                  fail_silently=False)
        messages.success(self.request, _('Message successfully sent'))
        return redirect('contact')
