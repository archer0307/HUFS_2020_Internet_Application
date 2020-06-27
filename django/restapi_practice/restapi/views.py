from django.shortcuts import render
from rest_framework import viewsets

from .models import ClientData
from .serializers import ClientDataSerializer


# Create your views here.

class ClientDataViewSet(viewsets.ModelViewSet):
	queryset = ClientData.objects.all()
	serializer_class = ClientDataSerializer