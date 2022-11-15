from django.test import TestCase

from task.models import Task
from api.serializers import TaskSerializer


class TestSerializer(TestCase):
    def test_task_serializer(self):
        '''Тестируем работу сериализатора'''
        test_task = Task.objects.create(
            title='test_title', text='test_text',
            done_date='2023-05-30'
        )
        data = TaskSerializer(test_task).data
        expected_data = {
            'title': test_task.title,
            'text': test_task.text,
            'done_date': test_task.done_date,
            'done': False
        }
        self.assertEqual(data, expected_data)
