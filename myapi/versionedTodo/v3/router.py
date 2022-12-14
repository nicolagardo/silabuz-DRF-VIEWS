from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todos', api.TodoViewSetCustom, 'todosCustom')

api_urlpatterns = router.urls
