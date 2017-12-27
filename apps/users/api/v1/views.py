from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.seriailizers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self, **kwargs):
        qs = self.queryset
        if self.kwargs.get('pk') == 'me':
            return qs.filter(id=self.request.user.id)
        return qs

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        if self.kwargs[lookup_url_kwarg] == 'me':
            return self.get_queryset().get()
        return super().get_object()
