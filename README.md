Добрый день!

Описание проекта

Проект представляет из себя сервис для отслеживания заданий, вы можете создавать новые задания, удалять, отмечать, как сделанные, выводить 1 задание или полный список заданий.

endpoints:

LIST_URL = '/api/v1/tasks/' - выводит список всех заданий(GET)
TASK_DATAIL_URL = '/api/v1/tasks/<int:id>' - выводит информацию о конкретном задании(GET)
CREATE_URL = '/api/v1/tasks/create/' - создает новое задание, по дефолту отметка о выполнении - False(POST)
DELETE_URL = '/api/v1/tasks/<int:id>/delete/' - удаляет задание по id(GET)
DONE_URL = '/api/v1/tasks/<int:id>/done/'  - меняет статус задания на выполненное(GET)
NOT_DONE_URL = '/api/v1/tasks/<int:id>/not-done/' - меняет статус задания на невыполненное(GET)

Для запуска проекта необходимо:

1. Установить виртуальное окружение (python -m venv venv)
2. Установить зависимости (pip install -r requirements.txt)
3. Перейти в папку task_list(cd task_list)
4. Сделать миграции (python manage.py migrate)
5. Запустить сервер(python manage.py runserver)
6. Перейти в приложени едля работы с API(например: Postman)

Спасибо! 
Хорошей работы!
