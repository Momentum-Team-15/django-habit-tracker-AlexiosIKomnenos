from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Record
from habit.forms import HabitForm, RecordForm
from django.contrib.auth.decorators import login_required



def index(request): 
    habits = Habit.objects.all()
    return render(request, 'habit/index.html', {'habits': habits})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    records = Record.objects.all()
    return render(request,'habit/habit_detail.html',{'records':records,'habit':habit})


def create_habit(request): 
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("home")
            
    else: 
        form = HabitForm()
        # if user is visting a page with GET request, not submitting the form yet
    return render(request, 'habit/create_habit.html', {'form': form})

def edit(request, habitpk):
    habit = get_object_or_404(Habit, pk=habitpk)
    if request.method == "POST":
        form = HabitForm(request.POST, request.FILES, instance=habit)
        if form.is_valid():
            habit = form.save()
            habit.user = request.user
            habit.created_at = timezone.now()
            habit.save()
            return redirect('home')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit/edit.html', {'form': form})



def habit_delete(request, habitpk):
    habit = Habit.objects.get(pk=habitpk)
    habit.delete()
    return redirect('home')

@login_required
def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')

def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            return redirect("home")
    else: 
        form = RecordForm()
    return render(request, 'habit/create_record.html', {'form': form})

def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('habit_detail', pk=record.pk)
    else:
        form = RecordForm(instance=record)
    return render(request, 'habit/edit_record.html', {'form': form})