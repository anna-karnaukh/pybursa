from django.shortcuts import render
from students.models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})


def students_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/student.html', {'student': student})
