from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def to_representation(self, instance):
        # Check if the request method is GET
        if self.context['request'].method == 'GET':
            # Remove 'write_only' attribute from 'password' field
            self.fields['password'].write_only = False

        return super().to_representation(instance)
    
    