from rest_framework import fields, serializers
from accounts.models import Address, NewUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import ugettext_lazy as _



class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    news_letter = serializers.BooleanField(default=False)
    class Meta:
        model = NewUser
        fields = ('email', 'user_name','first_name','last_name', 'password','news_letter')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        """
        Check that the email does exists.
        """
        if NewUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists!.")
        return value

    def validate_user_name(self, value):
        """
        Check that the user_name does exists.
        """
        if NewUser.objects.filter(user_name=value).exists():
            raise serializers.ValidationError("This username already exists!.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': _('Incorrect password')
        }
    def validate(self, attrs):
        email = attrs.get('email')
        if NewUser.objects.filter(email=email).exists():
            data = super().validate(attrs)
            return data
        raise serializers.ValidationError({'email': 'Account does not exist'})
        
    def get_token(cls, user):
        token = super().get_token(user)
        token['user'] = user.user_name
        return token

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'first_name','last_name','about')
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'