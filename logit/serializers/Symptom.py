from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from logit.models import Symptom

class SymptomSerializer(DynamicModelSerializer):
    user = DynamicRelationField('logit.serializers.UserSerializer')

    class Meta:
        model = Symptom
        name = 'symptom'
        fields = ('id', 'location', 'severity', 'pain_type', 'user', 'created_at', 'updated_at')
