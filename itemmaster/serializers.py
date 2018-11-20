from rest_framework import serializers
from .models import itemmaster

class itemmasterserializer(serializers.ModelSerializer):
    class Meta:
        model = itemmaster
        fields = ('itemcode','itemname')


