from rest_framework import serializers

from usr.models import *

class UsuariosBodegueroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuarios
        fields = '__all__'