from django.urls import path

from .views import (
    task_list, task_detail,
    create_task, delete_task,
    done_task, not_done_task
)


urlpatterns = [
    path('tasks/', task_list),
    path('tasks/<int:id>/', task_detail),
    path('tasks/create/', create_task),
    path('tasks/<int:id>/delete/', delete_task),
    path('tasks/<int:id>/done/', done_task),
    path('tasks/<int:id>/not-done/', not_done_task)
]
