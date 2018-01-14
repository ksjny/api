from dynamic_rest.viewsets import DynamicModelViewSet

from logit.serializers import UserSerializer
from logit.models import User

class UserViewSet(DynamicModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            self.kwargs['pk'] = self.request.user.pk

        return super(UserViewSet, self).get_object()
