from rest_framework import serializers
from Teacher.models import Teacher

from drf_dynamic_fields import DynamicFieldsMixin

class TeacherSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','name', 'lastName', 'gender', 'age', 'yearsOfExperience', 'birthday')