import subprocess

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Hero, Group
from app.serializers import HeroSerializer, GroupSerializer, UserSerializer


class UsersView(viewsets.ViewSet):

    @swagger_auto_schema(operation_id="Returns info about the logged user", tags=['Users'])
    def get(self, request, user_id, *kwargs):
        """

        Returns info about the logged user
        """
        try:
            usr = User.objects.get(id=user_id)
            return JsonResponse({"response": model_to_dict(usr)}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse({"error": f"Not found ID {user_id}"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_id="List all registered users", tags=['Users'])
    def list(self, request, *kwargs):
        """

        List of all registered users
        """
        users = [{'id': x.id, 'name': x.username} for x in User.objects.all()]
        return JsonResponse({"response": users}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_id="Creates a new user", tags=['Users'], request_body=UserSerializer)
    def create_new_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Hide password from output
            return Response({k: v for k, v in serializer.data.items() if 'password' != k},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroesView(viewsets.ViewSet):

    @swagger_auto_schema(operation_id="Returns hero data", tags=['Heroes'])
    def get(self, request, hero_id, *kwargs):
        """

        Returns information about one specific hero
        """
        try:
            hero = Hero.objects.get(hero_id=hero_id)
            return JsonResponse({"response": model_to_dict(hero)}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse({"error": f"Not found {hero_id}"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_id="Filter heroes by group", tags=['Heroes'])
    def filter(self, request, hero_id, *kwargs):
        """

        Returns information about one specific hero
        """
        try:
            heroes = Hero.objects.filter(group_id=hero_id)
            return JsonResponse({"response": [model_to_dict(hero) for hero in heroes]}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error - {e}"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_id="Returns a list of heroes", tags=['Heroes'])
    def list(self, request, *kwargs):
        """

        Return full list of heroes
        """
        heroes = [model_to_dict(x) for x in Hero.objects.all()]
        return JsonResponse({"response": heroes}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_id="Edit hero data", tags=['Heroes'], request_body=HeroSerializer,
                         manual_parameters=[openapi.Parameter('hero_id', openapi.IN_QUERY, required=False,
                                                              description='Hero ID', type=openapi.TYPE_INTEGER)])
    def post(self, request, *kwargs):
        """

        **Edit a hero.**
        If a hero_id is passed as query, it will search and update the instance. If no hero_id it will verify if the name \
        is unique and create a new instance.
        To move one hero from a group to another, pass the hero_id as query and the group in the body.

        **Example**

        `/api/heroes/upsert/?hero_id=1017851`

        ```
        {
          "group_id": 2
        }
        ```
        """

        try:

            data = request.data
            hero_id = request.query_params.get('hero_id')
            name = data.get('name')

            instance = Hero.objects.filter(Q(hero_id=hero_id) | Q(name=name)).first()

            serializer = HeroSerializer(instance=instance, data=data)
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
        except Exception as e:
            return JsonResponse({"error": f"Fatal: " + str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_id="Delete a hero", tags=['Heroes'],
                         manual_parameters=[openapi.Parameter('hero_id', openapi.IN_PATH,
                                                              description="ID of the model to delete",
                                                              type=openapi.TYPE_INTEGER)])
    def delete(self, request, hero_id):
        try:
            instancia = Hero.objects.get(pk=hero_id)
            instancia.delete()
            return Response({"response": "Object deleted"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"response": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)


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

    @swagger_auto_schema(operation_id="Edit group", tags=['Groups'], request_body=GroupSerializer,
                         manual_parameters=[openapi.Parameter('group_id', openapi.IN_QUERY, required=False,
                                                              description='Group ID', type=openapi.TYPE_INTEGER)])
    def post(self, request, *kwargs):
        """

        Edits a group.
        If a group_id is passed as query, it will search and update the instance. If no group_id it will verify if the name \
        is unique and create a new instance.
        """

        data = request.data
        group_id = request.query_params.get('group_id')
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


@swagger_auto_schema(methods=['get'], operation_id="Populate heroes from official Marvel website", tags=['Heroes'])
@api_view(['GET'])
def update_marvel_heroes_endpoint(request):
    try:
        subprocess.run(['python3', 'manage.py', 'update_marvel_heroes'], check=True)
        return JsonResponse({'message': 'Comando update_marvel_heroes executado com sucesso'})
    except subprocess.CalledProcessError as e:
        return JsonResponse({'message': f'Erro ao executar o comando: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

