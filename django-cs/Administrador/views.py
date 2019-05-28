# -----------------LIBRERIAS----------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# -----------------MODELOS-------------------
     #Nombre App                 Nombre modelo
from Administrador.models import Administrador

# ------------SERIALIZERS--------------------
from Administrador.serializers import AdministradorSerializers

# ------------LIBRERIAS EXTERNAS-----------------
# import json

class AdministradorList(APIView):
    
    # METODO PARA SOLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Administrador.objects.filter(delete = False)
        serializer = AdministradorSerializers(queryset, many=True)
        return Response(serializer.data)

    # METODO PARA CREAR NUEVO REGISTRO
    def post(self, request, format=None):
        serializer = AdministradorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status=status.HTTP_201_CREATED)

class AdministradorDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, pk):
        try:
            return Administrador.objects.get(pk=pk)
        except Administrador.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, pk, format=None):
        print("Este es el id: " + pk)
        Id = self.get_object(pk)
        if Id != "No":
            Id = AdministradorSerializers(Id)
            return Response(Id.data)
        return Response("No Existe")
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = AdministradorSerializers(Id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)



