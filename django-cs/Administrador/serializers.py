# ----------------LIBRERIAS-----------------
from rest_framework import routers, serializers, viewsets

# -----------------MODELOS-------------------
     #Nombre App                 Nombre modelo
from Administrador.models import Administrador

class AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('id','name','ap_pat','ap_mat','year')

