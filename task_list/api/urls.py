from rest_framework import routers
from django.urls import include, path

from .views import (
    task_list, one_task,
    create_task, delete_task,
    done_task
)


urlpatterns = [
    path('tasks/', task_list),
    path('tasks/<int:id>/', one_task),
    path('tasks/create/', create_task),
    path('tasks/<int:id>/delete/', delete_task),
    path('tasks/<int:id>/done/', done_task)
]
