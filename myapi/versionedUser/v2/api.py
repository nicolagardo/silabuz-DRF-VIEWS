from rest_framework import viewsets
from rest_framework import mixins

from .serializer import UserSerializer
from users.models import Users



# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

class UserViewSetOne(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin, 
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    lookup_field = 'username'

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

