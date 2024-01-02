from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import clientSerializer
from django.http import JsonResponse

@api_view(['POST'])
def client_list(request): 
    if request.method == 'POST':
        serializer = clientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_client_detail(request, id):
    try:
        client_instance = Client.objects.get(id=id)
    except Client.DoesNotExist:
        return Response(status=400)
    serializer = clientSerializer(client_instance)
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def update_client_detail(request, pk):
    try:
        client_instance = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=404)

    serializer = clientSerializer(client_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_client(request, pk):
    try:
        client_instance = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=404)
    #Delete user
    client_instance.delete()
    return Response("deleted",status=204)
