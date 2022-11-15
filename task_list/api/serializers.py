from datetime import date

from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    done_date = serializers.DateField()

    class Meta:
        fields = '__all__'
        model = Task

    def validate_done_date(self, data):
        now = date.today()
        if now > data:
            raise serializers.ValidationError(f"Вы не можете указать дату меньше чем {now}")
        return data
    
    def validate_title(self, title):
        obj = Task.objects.filter(title=title, done = 'False')
        if obj:
            raise serializers.ValidationError(
                f"Вы указали задание с существующим названием, закройте предыдущую задачу, либо переименуйте данную"
            )
        return title
