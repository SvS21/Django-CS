# ------------Librerias------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Profile.models import Profile
# ----------------serializers-------------
from Profile.serializers import ProfileSerializers

# ------------------LIBRERIAS EXTERNAS------------------
# import json

class ProfileList(APIView):
    # METODO PARA EXPLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Profile.objects.filter(delete = False)
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)
    # METODO PARA CREAR NUEVO REGISTRO 
    def post(self, request, format=None):
        serializer = ProfileSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas, status=status.HTTP_201_CREATED)

class ProfileDetail(APIView):
    #METODO PARA COSULTAR ID Y E RETORNE SI EXISTE O NO
    def get_object(self,pk):
        try: 
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return "No"
    #METODO PARA CONSULTAR ID Y DEVOLVER LOS VALORES DE SUS CAMPOS 
    def get(self, request,pk, format=None):
        print("Este es el id:"+pk)
        Id = self.get_object(pk) 
        if Id != "No":
            Id = ProfileSerializers(Id)
            return Response(Id.data)
        return Response("No existe")
    #METODO CONSULTAR ID Y ACTUALIZAR DATOS 
    def put(self, request,pk, format=None):
        Id = self.get_object(pk)
        serializer = ProfileSerializers(Id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response("Error", status.HTTP_400_BAD_REQUEST)