from rest_framework import serializers
from app.models import Assets

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'assetfile',
            'date_time',
            'user',
        )
        model = Assets

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('name','assetfile',)