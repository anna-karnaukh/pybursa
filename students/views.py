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


class StudentForm(forms.ModelForm):
    error_css_class = 'errorList'
    class Meta:
        model = Student


def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            student = form.save()
            return redirect('/students')
    form = StudentForm(instance = student)
    return render(request, 'students/edit.html',{'form': form})


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('/students')
        return render(request, 'students/edit.html',{'form': form})
    form = StudentForm()
    return render(request, 'students/edit.html',{'form': form})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('/students') 
