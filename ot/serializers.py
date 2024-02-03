from rest_framework import serializers
from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = "__all__"
