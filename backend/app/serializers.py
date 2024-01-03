from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Hero, Group


class HeroSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Hero
        exclude = ('hero_id', 'group')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

