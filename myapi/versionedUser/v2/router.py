from rest_framework.routers import Route, SimpleRouter, DefaultRouter
from . import api
class CustomRouter(SimpleRouter):
    routes = [
        Route(
            url = r'^{prefix}$',
            mapping = {'get':'get'},
            name = '{basename}-list',
            detail = False,
            initkwargs= {'suffix':'List'}
        ),
        Route(
            url = r'^{prefix}$',
            mapping = {'get':'retrieve'},
            name = '{basename}-detail',
            detail = True,
            initkwargs= {'suffix':'Detail'}
        ),
        Route(
            url = r'^{prefix}$',
            mapping = {'post':'post'},
            name = '{basename}-create',
            detail = True,
            initkwargs= {'suffix':'Create'}
        ),
        Route(
            url = r'^{prefix}$',
            mapping = {'put':'put'},
            name = '{basename}-update',
            detail = True,
            initkwargs= {'suffix':'Update'}
        ),
    ]

router = DefaultRouter()
router.register(r'users', api.UserViewSet, 'todosCustom')

api_urlpatterns = router.urls