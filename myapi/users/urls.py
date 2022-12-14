from rest_framework import routers

from .api import UserViewSet, UserViewSetOne


router = routers.DefaultRouter()

router.register('/v1/users', UserViewSet, 'users')
router.register('/v1/users', UserViewSetOne, 'oneuser')


urlpatterns = router.urls