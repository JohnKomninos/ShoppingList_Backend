from rest_framework import serializers
from .models import Sublist

class SublistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sublist
        fields = ('id', 'name', 'category', 'aisle', 'quantity')
