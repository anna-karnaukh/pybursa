from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from coaches.models import Coach

def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/coaches.html', {'coaches': coaches})


def coaches_item(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, 'coaches/coach.html', {'coach': coach})


class CoachModelForm(forms.ModelForm):
    error_css_class = 'errorList'
    class Meta:
        model = Coach


def coach_edit(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    if request.method == 'POST':
        form = CoachModelForm(request.POST, instance=coach)
        if form.is_valid():
            coach = form.save()
            return redirect('/coaches', coach_id)
        else:
            return render(request, 'coaches/edit.html',{'form': form})
    else:
        form = CoachModelForm(instance=coach)
        return render(request, 'coaches/edit.html', {'form': form})


def coach_add(request):
    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
            coach = form.save()
            return redirect('/coaches')
        else: 
            return render(request, 'coaches/edit.html',{'form': form})
    else:
        form = CoachModelForm()
        return render(request, 'coaches/edit.html',{'form': form})


def coach_delete(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    coach.delete()
    return redirect('/coaches')
