from django.shortcuts import render

# rest_framework imports
from rest_framework import generics, status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

# models import
from app import Assets

# serializers import
from . import serializers

class ListAssets(generics.ListCreateAPIView):
    queryset = models.Assets.objects.all()
    serializer_class = serializers.AssetSerializer

class DetailAssets(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Assets.objects.all()
    serializer_class = serializers.AssetSerializer
