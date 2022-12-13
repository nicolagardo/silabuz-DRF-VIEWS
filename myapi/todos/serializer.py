from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
            "created_at",
            "updated_at",
            "deleted_at",
            "done_at",
            "status",
        )
        read_only_fields = "created_at", "updated_at", "deleted_at"

