from rest_framework.serializers import CharField, DateTimeField
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from logit.models import User

class UserSerializer(DynamicModelSerializer):
    password = CharField(required=True, write_only=True)
    firstName = CharField(required=False, source='first_name')
    lastName = CharField(required=False, source='last_name')
    createdAt = DateTimeField(read_only=True, source='date_joined')
    lastLogin = DateTimeField(read_only=True, source='last_login')

    class Meta:
        model = User
        name = 'user'
        fields = ('id', 'email', 'firstName', 'lastName', 'password', 'createdAt', 'lastLogin')
