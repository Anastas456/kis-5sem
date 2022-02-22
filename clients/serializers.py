from dataclasses import fields
from rest_framework import serializers
from .models import Client, Russian_passport, International_passport

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class RussianPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Russian_passport
        fields = '__all__'

class InternationalPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = International_passport
        fields = '__all__'

