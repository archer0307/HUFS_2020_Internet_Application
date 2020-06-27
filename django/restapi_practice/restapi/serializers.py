from rest_framework import serializers
from .models import ClientData

class ClientDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClientData
		fields = ('identification','password','phone_number','name',)
