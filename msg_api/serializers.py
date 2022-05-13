from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageConfirm
        fields = '__all__'

