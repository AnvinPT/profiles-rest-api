from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtokens.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions
from rest_framework import filters
# Create your views here.

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self, request, format =None):
        an_apiview = [
        'Use HTTP Methods as function(get, post, put, patch, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'IS Mapped manually to URLs',
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        a_viewset = [
        'Uses actions(list,create,retrieve,update,partial_update,destroy)',
        'Automatically maps to URLs using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message':message,'a_viewset':a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request):
        return Response({'method':'GET'})

    def update(self, request):
        return Response({'method':'PUT'})

    def partial_update(self, request):
        return Response({'method':'PATCH'})

    def destroy(self, request):
        return Response({'method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authenticationclasses = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)



class UserLoginApiView(ObtainAuthToken):
    renderer _classes = api_settings.DEFAULT_RENDERER_CLASSES
    
