from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import views
from django.http import JsonResponse
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from app.models import Hero, Group
from app.serializers import HeroSerializer, GroupSerializer


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


class GroupsView(viewsets.ViewSet):

    @swagger_auto_schema(operation_id="Returns group data", tags=['Groups'])
    def get(self, request, group_id, *kwargs):
        """

        Returns information about one specific group
        """
        try:
            hero = Group.objects.get(group_id=group_id)
            return JsonResponse({"response": model_to_dict(hero)}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse({"error": f"Not found {group_id}"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_id="Returns a list of groups", tags=['Groups'])
    def list(self, request, group_id=None, *kwargs):
        """

        Return full list of groups
        """
        heroes = [model_to_dict(x) for x in Group.objects.all()]
        return JsonResponse({"response": heroes}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_id="Edit group", tags=['Groups'], request_body=GroupSerializer)
    def post(self, request, group_id=None, *kwargs):
        """

        Edits a group.
        If a group_id is passed in path, it will update the instance. If no group_id it will verify if the name \
        is unique and create a new instance.
        """

        data = request.data
        name = data.get('name')

        instance = Group.objects.filter(Q(group_id=group_id) | Q(name=name)).first()

        serializer = GroupSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'response': serializer.validated_data}, status=status.HTTP_200_OK)
        else:
            existing = {}
            if instance:
                existing = model_to_dict(instance)
            return JsonResponse({'response': existing, 'extra_info': f"The editing didn't work: " +
                                                                     str(serializer.errors)},
                                status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_id="Delete a group", tags=['Groups'],
                         manual_parameters=[openapi.Parameter('group_id', openapi.IN_PATH,
                                                              description="ID of the model to delete",
                                                              type=openapi.TYPE_INTEGER)])
    def delete(self, request, group_id):
        try:
            instancia = Group.objects.get(pk=group_id)
            instancia.delete()
            return Response({"response": "Object deleted"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"response": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
