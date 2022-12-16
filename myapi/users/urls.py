from django.urls import re_path, include, path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from versionedUser.v2.router import api_urlpatterns as api_v2_u

from .api import UserViewSet, UserViewSetOne, SignUpView, GetUsers, LoginView


router = routers.DefaultRouter()

router.register('/v1/users', UserViewSet, 'users')
router.register('/v1/users', UserViewSetOne, 'oneuser')
router.register("", GetUsers)

urlpatterns = [
    path("/signup/", SignUpView.as_view(), name= "signup"),
    path("/login/", LoginView.as_view(), name= "login"),
    path("/jwt/create", TokenObtainPairView.as_view(), name="jwt_create"),
    path("/jwt/refresh", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("/jwt/verify", TokenVerifyView.as_view(), name="jwt_verify"),
]

re_path('/v2/users', include(api_v2_u)),

urlpatterns += router.urls