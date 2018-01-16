from rest_framework import serializers
from .models import RestUserProfile
from django.contrib.auth.models import User

class RestUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestUserProfile
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class RestUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance