from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from logit.models import Medication

class MedicationSerializer(DynamicModelSerializer):
    user = DynamicRelationField('logit.serializers.UserSerializer')

    class Meta:
        model = Medication
        name = 'medication'
        fields = ('id', 'name', 'time_period', 'user', 'created_at', 'updated_at')
