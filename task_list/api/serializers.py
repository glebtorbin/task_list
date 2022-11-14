from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)
    done_date = serializers.DateField()

    class Meta:
        fields = '__all__'
        model = Task