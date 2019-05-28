from rest_framework import serializers
from Student.models import Student

from drf_dynamic_fields import DynamicFieldsMixin

class StudentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name', 'lastName','registrationNumber', 'gender', 'age', 'telephoneNumber', 'address', 'subject', 'birthday','teacher')