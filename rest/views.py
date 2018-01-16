from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import RestUserProfile
from .serializers import RestUserProfileSerializer, UserLoginSerializer, RestUserSerializer
from django.contrib.auth import login, logout, authenticate

# Create your views here.

class UserList(APIView):

    def get(self, request):
        userList = RestUserProfile.objects.all()
        serializer = RestUserProfileSerializer(userList, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class UserLogin(APIView):

    def post(self, request):
        username = request.POST.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        print(user.password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user = User.objects.get(id=user.id)
                serializer = RestUserSerializer(user, many=False)
                # data = {'message': 'login success', 'last_login': user}
                return Response(serializer.data)
        return Response({'username': username, 'password': password})


class UserRegister(APIView):

    def post(self, request):
        # user = User
        # user.username = request.POST.get('username')
        # user.password = request.data.get('password')
        # user.email = request.POST.get('email')
        # user.first_name = request.data.get('first_name')
        # user.last_name = request.POST.get('last_name')
        serializer = RestUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'good'})
        # print(user.username)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class ChangeDesc(APIView):
#     def post(self, request):




