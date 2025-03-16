from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Include all fields from the Task model

    def validate_due_date(self, value):
        # Custom validation to ensure due_date is not in the past
        if value and value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value