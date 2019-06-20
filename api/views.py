from django.shortcuts import render

# rest_framework imports
from rest_framework import generics, status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

# models import
from app.models import Assets

# serializers import
from . import serializers

class ListAssets(generics.ListCreateAPIView):
    queryset = Assets.objects.all()
    serializer_class = serializers.AssetSerializer

class DetailAssets(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = serializers.AssetSerializer

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        asset_serializer = serializers.FileSerializer(data=request.data)

        if asset_serializer.is_valid():
            asset_serializer.save()
            return Response(asset_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(asset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)