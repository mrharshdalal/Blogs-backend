
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db import IntegrityError

@api_view(['POST', 'GET'])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserRegistrationSerializer(data = data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError as e:
                return Response({'error': 'Username already exists'})
        else:
            # print(serializer.errors) 
            return Response(serializer.errors)
        
    elif request.method == 'GET':
        users = User.objects.all()
        serialized_users = UserRegistrationSerializer(users, many=True, context={'request': request})
        return Response(serialized_users.data)
    
    else:
        return Response({'error': 'Method not allowed'})

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'})

        user = authenticate(username=username, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            # Generate or retrieve the user's authentication token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
