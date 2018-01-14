from dynamic_rest.viewsets import DynamicModelViewSet

from logit.models import Symptom
from logit.serializers import SymptomSerializer

class SymptomViewSet(DynamicModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = ()
