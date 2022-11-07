from rest_framework import serializers
from todo_app.models import Task


class TodoSerializer(serializers.ModelSerializer):  # серіалізатор моделі Task
    class Meta:
        model = Task
        fields = ('id', 'text', 'is_published', 'created_at', 'updated_at')

