from rest_framework import serializers

from ntf.models import *

class NotificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notificacion
        fields = '__all__'