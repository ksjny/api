from dynamic_rest.viewsets import DynamicModelViewSet

from logit.models import Medication
from logit.serializers import MedicationSerializer

class MedicationViewSet(DynamicModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = ()
