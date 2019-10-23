from django.urls import path

from . import views

urlpatterns = [
path('todo/', views.todoview),
path('addTodo/', views.addTodo),
path('deleteTodo/', views.deleteTodo),
]