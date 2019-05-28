from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from Student.models import Student
from Student.serializers import StudentSerializer

class StudentList(APIView):
    def get (self, request, format=None):
        queryset = Student.objects.filter(registrationNumber=181086, subject="Cliente-Servidor", age=19, gender="Hombre")
        serializer = StudentSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class StudentDetail(APIView):
  # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Student.objects.get(pk=id)
        except Student.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        # print("Este es el id: " + id)
        student = self.get_object(id)
        # if student != "No":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
        # return Response("No Existe")
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)