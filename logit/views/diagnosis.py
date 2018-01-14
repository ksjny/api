from dynamic_rest.viewsets import DynamicModelViewSet

from logit.models import Diagnosis
from logit.serializers import DiagnosisSerializer

class DiagnosisViewSet(DynamicModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = ()
