from rest_framework import serializers
from .models import *

class sample(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    mark=serializers.IntegerField()
    subject=serializers.CharField()


class model_serializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'