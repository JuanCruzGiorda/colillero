from rest_framework import serializers
from .models import Colillas, Colillero

class ColillasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colillas
        fields = '__all__'

class ColilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colillero
        fields = '__all__'