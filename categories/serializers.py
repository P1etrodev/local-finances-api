from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
	amount = serializers.IntegerField(read_only=True)
	
	class Meta:
		model = Category
		fields = '__all__'