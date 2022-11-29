from django.shortcuts import render
from .models import Sessions
from .serializers import SessionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def Index(request):
    return render(request, 'Index.html')

@api_view(['GET'])
def SessionsAPI(request):
    session = Sessions.objects.all().order_by('id')
    serializer = SessionSerializer(session, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def SessionDetailsAPI(request, id):
    Sessions = get_object_or_404(Sessions, id=id)
    serializer = SessionSerializer(session, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddSessionAPI(request):
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditSessionAPI(request, id):
    session = get_object_or_404(Sessions, id=id)
    serializer = SessionSerializer(session, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def DeleteSessionAPI(request, id):
    if request.is_ajax():
        ession = get_object_or_404(Sessions, id=id)
        session.delete()
        return Response('Session exercise successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Session Doesn't Exists!", status=status.HTTP_204_NO_CONTENT)