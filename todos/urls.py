from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.getTodos , name='getTodos'),
    # path('todos/<int:pk>/', views.getTodo),
    # path('todos/', views.createTodo),
    # path('todos/<int:pk>/', views.updateTodo),
    # path('todos/<int:pk>/', views.deleteTodo),
]