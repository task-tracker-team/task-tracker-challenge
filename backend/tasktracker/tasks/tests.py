from django.test import TestCase
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer

class TaskTests(TestCase):
    def test_create_task_with_missing_title(self):
        data = {'description': 'Test description'}
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_update_status_to_completed(self):
        task = Task.objects.create(title='Test Task', status='Pending')
        task.status = 'Completed'
        task.save()
        self.assertEqual(task.status, 'Completed')

    def test_filter_tasks_by_status(self):
        Task.objects.create(title='Task 1', status='Pending')
        Task.objects.create(title='Task 2', status='Completed')
        response = self.client.get('/api/tasks/?status=Completed')
        self.assertEqual(len(response.data['results']), 1)