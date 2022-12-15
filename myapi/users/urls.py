from django.urls import re_path, include

from rest_framework import routers
from versionedUser.v2.router import api_urlpatterns as api_v2_u

from .api import UserViewSet, UserViewSetOne


router = routers.DefaultRouter()

router.register('/v1/users', UserViewSet, 'users')
router.register('/v1/users', UserViewSetOne, 'oneuser')

# re_path('/v2/', include())

re_path('/v2/users', include(api_v2_u)),

urlpatterns = router.urls