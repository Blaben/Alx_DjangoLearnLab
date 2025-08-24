from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
   serializers.CharField()
    Token.objects.create
    get_user_model().objects.create_user