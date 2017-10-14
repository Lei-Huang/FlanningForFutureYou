from rest_framework import serializers
from .models import BasicProfile,UserGroup
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicProfile
        fields =('profile_id','first_name','last_name','user_group','study_status')

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields =('name',)
