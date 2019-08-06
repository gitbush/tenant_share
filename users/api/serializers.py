from rest_framework import serializers
from users.models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('register_as', 
                      'profile_image', 
                  )
                  

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 
                  'username', 
                  'first_name', 
                  'last_name', 
                  'email',
                  'profile',
                  )