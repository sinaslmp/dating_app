from rest_framework import serializers
from .models import User, Gender

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'name']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    gender = serializers.PrimaryKeyRelatedField(queryset=Gender.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture', 'bio', 'gender', 'date_of_birth', 'location']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            profile_picture=validated_data.get('profile_picture'),
            bio=validated_data.get('bio'),
            gender=validated_data.get('gender'),
            date_of_birth=validated_data.get('date_of_birth'),
            location=validated_data.get('location')
        )
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    gender = GenderSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture', 'bio', 'gender', 'date_of_birth', 'location']
