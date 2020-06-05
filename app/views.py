from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from app.models import School, Student
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'app/index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school'
    model = School
    template_name = 'app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School
    success_url = reverse_lazy("app:school_list")

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("app:school_list")


class StudentListView(ListView):
    context_object_name = 'students'
    model = Student

class StudentDetailView(DetailView):
    context_object_name = 'student'
    model = Student
    template_name = 'app/student_detail.html'

class StudentCreateView(CreateView):
    fields = ('name', 'school')
    model = Student
    success_url = reverse_lazy("app:student_list")

class StudentUpdateView(UpdateView):
    fields = ('name', 'school')
    model = Student

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('app:student_list')
