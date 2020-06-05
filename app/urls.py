from django.contrib import admin
from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),

    path('school_list/', views.SchoolListView.as_view(), name='school_list'),
    path('school_list/<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('school_create/', views.SchoolCreateView.as_view(), name='school_create'),
    path('school_update/<int:pk>/', views.SchoolUpdateView.as_view(), name='school_update'),
    path('school_delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='school_delete'),

    path('student_list/', views.StudentListView.as_view(), name='student_list'),
    path('student_list/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student_create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student_update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student_delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
]