from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import views
from django.http import JsonResponse
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from app.models import Hero
from app.serializers import HeroSerializer


class UserDetailsView(views.APIView):

    @swagger_auto_schema(operation_id="Get info about the user logged", tags=['Users'])
    def get(self, request, token):
        user = get_user_model().objects.get(auth_token=token)
        return Response({
            'username': user.username
        })


class HeroesView(views.APIView):

    @swagger_auto_schema(operation_id="Return list of heroes", tags=['Heroes'])
    def get(self, request, *kwargs):
        heroes = [model_to_dict(x) for x in Hero.objects.all()]
        return JsonResponse({"response": heroes}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_id="Edit hero", tags=['Heroes'], request_body=HeroSerializer)
    def post(self, request, *kwargs):
        return JsonResponse({}, status=status.HTTP_200_OK)
