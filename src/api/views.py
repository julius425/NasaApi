from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import CADRecord
from api.serializers import CADRecordSerializer


class CADRecordList(APIView):
    """
    List all CADRecords, or create a new CADRecord.
    """
    def get(self, request, format=None):
        CADRecords = CADRecord.objects.all()
        serializer = CADRecordSerializer(CADRecords, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CADRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CADRecordDetail(APIView):
    """
    Retrieve, update or delete a CADRecord instance.
    """
    def get_object(self, pk):
        try:
            return CADRecord.objects.get(pk=pk)
        except CADRecord.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        CADRecord = self.get_object(pk)
        serializer = CADRecordSerializer(CADRecord)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        CADRecord = self.get_object(pk)
        serializer = CADRecordSerializer(CADRecord, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        CADRecord = self.get_object(pk)
        CADRecord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)