from rest_framework import serializers
from medicalstorapp.models import medicalstore

class medicalserializers(serializers.ModelSerializer):
    class Meta:
        model = medicalstore
        fields = '__all__'