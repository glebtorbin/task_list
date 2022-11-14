from rest_framework import routers
from django.urls import include, path

from .views import task_list, one_task, create_task


urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:id>/', one_task, name='one_task'),
    path('tasks/create/', create_task, name='create_task'),
]