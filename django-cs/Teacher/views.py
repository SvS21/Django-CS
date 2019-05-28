from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from Teacher.models import Teacher
from Teacher.serializers import TeacherSerializer

class TeacherList(APIView):
    def get (self, request, format=None):
        queryset = Teacher.objects.filter(age=30, yearsOfExperience=5, gender="Hombre")
        serializer = TeacherSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class TeacherDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Teacher.objects.get(pk=id)
        except Teacher.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        # print("Este es el id: " + id)
        teacher = self.get_object(id)
        # if Id != "No":
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
        # return Response("No Existe")
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        Id = self.get_object(id)
        serializer = TeacherSerializer(Id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)