from rest_framework import serializers
from .models import EngineeringData, DatasetRequest, DatasetResponse, ProjectModel, FinalModel

class EngineeringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineeringData
        fields = '__all__'

class DatasetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetRequest
        fields = '__all__'

class DatasetResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetResponse
        fields = '__all__'

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'

class FinalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalModel
        fields = '__all__'
