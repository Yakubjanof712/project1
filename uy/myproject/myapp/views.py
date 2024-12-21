from django.shortcuts import render, redirect
from .forms import CourseForm, LessonForm, TurlarForm, GullarForm
from django.shortcuts import render
from .models import Course

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'create_lesson.html', {'form': form})

def create_turlar(request):
    if request.method == 'POST':
        form = TurlarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turlar_list')
    else:
        form = TurlarForm()
    return render(request, 'create_turlar.html', {'form': form})

def create_gullar(request):
    if request.method == 'POST':
        form = GullarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gullar_list')
    else:
        form = GullarForm()
    return render(request, 'create_gullar.html', {'form': form})



def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'myapp/home.html')



def course_list(request):
    courses = Course.objects.all()
    return render(request, 'myapp/course_list.html', {'courses': courses})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'myapp/create_course.html', {'form': form})



def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'myapp/lesson_list.html', {'lessons': lessons})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'myapp/course_list.html', {'courses': courses})