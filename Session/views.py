from django.shortcuts import render, redirect
from .models import Sessions
from .serializers import SessionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required



def dashboard(request):
    return render(request, 'dashboard.html')


def Index(request):
    return render(request, 'Index.html')


def signup(request):
    # sign up new user and redirect to login page
    if request.method == "POST":
        if request.POST.get('singup'):
            full_name = request.POST.get('full_name')
            username = request.POST.get('username')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=full_name)
                print("user created")
                user.save()
                return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    # login user and redirect to index page
    if request.method == "POST":
        if request.POST.get('signin'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            if password and username:
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('signin')
    return render(request, 'signin.html')


def signout(request):
    # logout user and redirect to login page
    logout(request)
    return redirect('dashboard')


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



def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})