from rest_framework import serializers
from rest_framework.response import Response
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'




class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viajem
        fields = '__all__'



    def get(self, request   ):
        pass