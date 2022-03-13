from rest_framework import viewsets
from rest_framework import permissions
from .models import Client, Russian_passport, International_passport
from .serializers import ClientSerializer, RussianPassportSerializer, InternationalPassportSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

class RussianPassportViewSet(viewsets.ModelViewSet):
    queryset = Russian_passport.objects.all()
    serializer_class = RussianPassportSerializer
    permission_classes = [permissions.AllowAny]

class InternationalPassportViewSet(viewsets.ModelViewSet):
    queryset = International_passport.objects.all()
    serializer_class = InternationalPassportSerializer
    permission_classes = [permissions.AllowAny]