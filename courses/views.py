from django import forms 
from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})


def courses_item(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course.html', {'course': course})


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course


def course_edit(request, course_id):
    course= Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('/courses', course_id)
        else:
            return render(request, 'courses/edit.html',{'form': form})
    else:
        form = CourseModelForm(instance=course)
        return render(request, 'courses/edit.html', {'form': form})


def course_add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('/courses')
        else: 
            return render(request, 'courses/edit.html',{'form': form})
    else:
        form = CourseModelForm()
        return render(request, 'courses/edit.html',{'form': form})


def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('/courses')
