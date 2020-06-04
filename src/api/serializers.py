from api.models import CADRecord
from rest_framework import serializers


class CADRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CADRecord
        fields = '__all__'