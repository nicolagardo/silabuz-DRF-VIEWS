from django.contrib.auth import authenticate


from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer, SignUpSerializer, GetUserSerializer
from .models import Users, User
from .tokens import create_jwt_pair_for_user



# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()


class UserViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UserViewSetOne(
    mixins.RetrieveModelMixin, 
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    lookup_field = 'username'

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data

        # Atributo o variable para serializar
        ser = self.serializer_class(data=data)

        if ser.is_valid():
            ser.save()
            return Response(
                {"message":"El usuario se creó correctamente",
                  "data":ser.data},
                status= status.HTTP_201_CREATED
            )
        return Response(data= ser.errors, status= status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """ View para el logeo del usuario"""
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email= email, password= password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            resp = {"message":"Logeado correctamente",
                 "email": email,
                 "tokens": tokens
                 }
            return Response(data = resp, status=status.HTTP_200_OK)
        else: return Response(
            data={"message": "Correo inválido o contraseña incorrecta"}
            )

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data= content, status=status.HTTP_200_OK)


class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()