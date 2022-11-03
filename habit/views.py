from django.shortcuts import render, get_object_or_404
from .models import Habit
# Create your views here.

#this is the homepage, put @loginrequired later
def index(request): 
    habits = Habit.objects.all()
    return render(request, 'habit/index.html', {'habits': habits})

def habit_detail(request, pk):
    improvement = Improvement.objects.get(pk=pk)
    return render(request, 'habit/habit_detail.html', {'improvements': improvements})