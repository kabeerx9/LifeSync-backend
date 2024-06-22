from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.list_tasks , name='list-tasks'),
    path('tasks/create/', views.create_task , name='create-task'),
    path('tasks/edit/', views.edit_task , name='edit-task'),
    path('tasks/update/<int:pk>', views.update_task , name='update-task'),
    path('tasks/delete/<int:pk>', views.delete_task , name='delete-task'),
]