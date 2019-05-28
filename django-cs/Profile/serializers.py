# ----------------LIBRERIAS-----------------
from rest_framework import routers, serializers, viewsets

# -----------------MODELOS-------------------
     #Nombre App                 Nombre modelo
from Profile.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name','ap_pat','ap_mat','year','img')

