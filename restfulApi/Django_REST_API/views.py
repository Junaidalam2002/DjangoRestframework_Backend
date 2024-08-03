from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Data
from .serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DataViewset(APIView):
    
    def get(self, request, id=None):
        if id:
            item = Data.objects.get(id=id)
            serializer = DataSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Data.objects.all()
        serializer = DataSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Data.objects.get(id=id)
        serializer = DataSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = Data.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})