from datetime import date

from rest_framework.test import APITestCase

from task.models import Task
from api.serializers import TaskSerializer


class TestTasksViews(APITestCase):
    LIST_URL = '/api/v1/tasks/'
    TASK_DATAIL_URL = '/api/v1/tasks/'
    CREATE_URL = '/api/v1/tasks/create/'
    DELETE_URL = '/api/v1/tasks/{}/delete/'
    DONE_URL = '/api/v1/tasks/{}/done/'
    NOT_DONE_URL = '/api/v1/tasks/{}/not-done/'

    def test_task_list(self):
        '''Проверяем, что открывается полный список записей'''
        test_task_1 = Task.objects.create(
            title='test_title', text='test_text', done_date='2023-05-30'
        )
        test_task_2 = Task.objects.create(
            title='test_title_2', text='test_text_2', done_date='2023-05-30'
        )
        response = self.client.get(self.LIST_URL)
        self.assertEqual(
            TaskSerializer([test_task_1, test_task_2], many=True).data, response.data['tasks']
        )
    
    def test_task_detail(self):
        '''Проверяем, что открывается запись по id'''
        test_task = Task.objects.create(
            title='test_title', text='test_text', done_date='2023-05-30'
        )
        response = self.client.get(f'{self.TASK_DATAIL_URL}{test_task.id}/')
        serializer = TaskSerializer(data=response.data['task'], many=False)
        if serializer.is_valid():
            self.assertEqual(serializer.data, TaskSerializer(test_task).data)
    
    def test_task_create(self):
        '''Проверям, что создаются записи'''
        test_task = Task.objects.create(
            title='test_title', text='test_text',
            done_date='2023-05-30', done = True
        )
        self.client.post(
            self.CREATE_URL, data=TaskSerializer(test_task).data
        )
        self.assertEqual(Task.objects.count(), 2)
    
    def test_task_create_non_equal(self):
        '''Проверяем, что не создается незакрытых заданий с одинаковым названием'''
        test_task = Task.objects.create(
            title='test_title', text='test_text',
            done_date='2023-05-30', done = False
        )
        self.client.post(
            self.CREATE_URL, data=TaskSerializer(test_task).data
        )
        self.assertEqual(Task.objects.count(), 1)
    
    def test_create_date(self):
        '''Проверяем, что нельзя закрыть задание задним числом'''
        now = date.today()
        test_task = Task.objects.create(
            title='test_title', text='test_text',
            done_date='2021-05-30', done = False
        )
        self.client.post(
            self.CREATE_URL, data=TaskSerializer(test_task).data
        )
        self.assertEqual(Task.objects.count(), 1)
    
    def test_task_delete(self):
        '''Проверяем, что запись удаляется'''
        test_task = Task.objects.create(
            title='test_title', text='test_text',
            done_date='2021-05-30', done = False
        )
        self.client.get(
            self.DELETE_URL.format(test_task.id)
        )
        self.assertEqual(Task.objects.count(), 0)
    
    def test_task_done(self):
        '''Проверяем, что задание отмечается, как сделанное'''
        test_task = Task.objects.create(
            title='test_title', text='test_text',
            done_date='2021-05-30', done = False
        )
        self.client.get(self.DONE_URL.format(test_task.id))
        test_task = TaskSerializer(
            Task.objects.get(id=f'{test_task.id}')
        ).data
        self.assertEqual(TaskSerializer(test_task).data['done'], True)
    
    def test_task_not_done(self):
        '''Проверяем, что задание отмечается, как несделанное'''
        test_task = Task.objects.create(
            title='test_title', text='test_text',
            done_date='2021-05-30', done = True
        )
        self.client.get(self.NOT_DONE_URL.format(test_task.id))
        test_task = TaskSerializer(
            Task.objects.get(id=f'{test_task.id}')
        ).data
        self.assertEqual(TaskSerializer(test_task).data['done'], False)
