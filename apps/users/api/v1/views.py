from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.seriailizers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self):
        if self.kwargs.get(self.lookup_field) == 'me':
            self.kwargs[self.lookup_field] = self.request.user.id
        return super().get_object()
