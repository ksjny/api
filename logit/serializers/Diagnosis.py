from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from logit.models import Diagnosis

class DiagnosisSerializer(DynamicModelSerializer):
    user = DynamicRelationField('logit.serializers.UserSerializer')

    class Meta:
        model = Diagnosis
        name = 'diagnosis'
        fields = ('id', 'name', 'severity', 'user', 'created_at', 'updated_at')
