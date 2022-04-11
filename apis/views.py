from rest_framework import generics
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from . import serializers
from listazadan import models
from listazadan .models import Zadanie
from .serializers import ZadanieSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
        
    serializer_class = UserSerializer
    
    
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListZadanie(generics.ListCreateAPIView):
    
    #queryset = models.Zadanie.objects.all()
    serializer_class = ZadanieSerializer
    def get_queryset(self):
       
        
        if  self.request.user.is_superuser:
            return Zadanie.objects.all()
        else:
            user = self.request.user
            return Zadanie.objects.filter(user=user)

class ListZadanieUser(generics.ListCreateAPIView):
    
    #queryset = models.Zadanie.objects.all()
    serializer_class = ZadanieSerializer
    def get_queryset(self):
               
        
        
        return Zadanie.objects.filter(user=self.kwargs["user_id"])


class DetailZadanie(generics.RetrieveUpdateDestroyAPIView):
    
    #queryset = models.Zadanie.objects.all()
    serializer_class = ZadanieSerializer
    def get_queryset(self):
        
        
        if  self.request.user.is_superuser:
            return Zadanie.objects.all()
        else:
            user = self.request.user
            return Zadanie.objects.filter(user=user)
       

class DetailZadanieUser(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = models.Zadanie.objects.all()
    serializer_class = ZadanieSerializer
    


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)