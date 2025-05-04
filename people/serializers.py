from rest_framework import serializers

from .models import Person
from transactions.serializers import TransactionSerializer


class PersonSerializer(serializers.ModelSerializer):
	borrowed = serializers.FloatField(default=0, read_only=True)
	lended = serializers.FloatField(default=0, read_only=True)
	transactions = serializers.ListField(child=TransactionSerializer(), read_only=True)
	
	class Meta:
		model = Person
		fields = '__all__'