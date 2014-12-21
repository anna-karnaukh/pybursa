from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from students.models import Student, Dossier
from courses.models import Course


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})


def students_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/student.html', {'student': student})


class StudentForm(forms.Form):
    PACKAGE_CHOICE = (
        ('S', 'Standart'),
        ('G', 'Gold'),
        ('V', 'VIP'),
    )
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())
    package_choice = forms.ChoiceField(widget=forms.RadioSelect, 
                                     choices=PACKAGE_CHOICE)
    dossier = forms.ModelChoiceField(Dossier.objects.all(), required=False)



def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(initial=model_to_dict(student))
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student()
            for key, value in form.cleaned_data.iteritems(): 
                setattr(student, key, value)
            student.save()
            return redirect('/students')
        return render(request, 'students/edit.html', {'form': form})
    return render(request, 'students/edit.html',{'form': form})


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student()
            for key, value in form.cleaned_data.iteritems():
                    setattr(student, key, value)
            student.save()
            return redirect('/students')
        return render(request, 'students/edit.html',{'form': form})
    form = StudentForm()
    return render(request, 'students/edit.html',{'form': form})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('/students') 
