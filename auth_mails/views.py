from django.shortcuts import render, redirect
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Register view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        password1 = request.POST['pass2']
        email = request.POST['email']

        # Validate username
        if len(username) < 8:
            messages.error(request, 'Username must be at least 8 characters long.')
            return redirect('register')
        elif not re.search(r'[a-zA-Z0-9]', username):
            messages.error(request, 'Username must contain alphanumeric characters.')
            return redirect('register')

        # Validate email
        
        elif not email.endswith('@gmail.com'):
            messages.error(request, 'Email must end with @gmail.com')
            return redirect('register')

        # Validate password
        elif not password.isdigit():
            messages.error(request, "Password must contain only numeric characters.")
            return redirect('register')
        elif len(password) < 6 :
            messages.error(request, 'Password must be at least 6 characters long.')
            return redirect('register')

        # Passwords match
        if password == password1:
            # Check if email or username already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            else:
                # Create new user
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Your account has been created successfully.')
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
    else:
        return render(request, 'register.html')

# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'You are now logged in as {username}.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'login.html')

# Logout view
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')




# create authentication endpoints(API)


from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return Response({"message": "User logged in successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
