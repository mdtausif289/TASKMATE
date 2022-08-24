from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todolist/', views.todolist, name='todolist'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    path('edit_task/<task_id>', views.edit_task, name='edit_task'),
    path('complete_task/<task_id>', views.complete_task, name='complete_task'),
    path('pending_task/<task_id>', views.pending_task, name='pending_task'),
]
