from rest_framework.serializers import ModelSerializer
from .models import StudentClass

class StudentSerializer(ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ["name", "roll"]