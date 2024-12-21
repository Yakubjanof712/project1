from django import forms
from .models import Course, Lesson, Turlar, Gullar

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']

class TurlarForm(forms.ModelForm):
    class Meta:
        model = Turlar
        fields = ['name']

class GullarForm(forms.ModelForm):
    class Meta:
        model = Gullar
        fields = ['turlar', 'name']