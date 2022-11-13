from rest_framework import serializers
from teachers.models import *


class QuizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
