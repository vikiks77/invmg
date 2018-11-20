from django.shortcuts import render
from rest_framework import viewsets
from .models import itemmaster
from .serializers import itemmasterserializer

class itemmasterview(viewsets.ModelViewSet):
    queryset = itemmaster.objects.all()
    serializer_class = itemmasterserializer