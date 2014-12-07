from django.shortcuts import render
from courses.models import Course

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})


def courses_item(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course.html', {'course': course})
