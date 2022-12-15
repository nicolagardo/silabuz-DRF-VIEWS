from django.urls import path
from rest_framework import routers
from django.urls import re_path, include
from versionedTodo.v3.router import api_urlpatterns as api_v3
from versionedTodo.v4.router import api_urlpatterns as api_v4



from .api import AllTodo, OneTodo, TodoViewSetCustom, TodoViewSet



router = routers.SimpleRouter()

router.register('/v1/todos', TodoViewSetCustom)
router.register('/v2/todos', TodoViewSet)

urlpatterns = [

    path('/todos/all', AllTodo.as_view()),
    path('/todos/create', AllTodo.as_view()),
    path('/todos/one/<int:pk>', OneTodo.as_view()),
    # path('/todos/todos', TodoViewSetCustom.as_view({'get': 'list'})),
    # path('/todos/todos', TodoViewSetCustom.as_view({'get': 'list'})),
    # path('/todos/todos/<int:pk>', TodoViewSetCustom.as_view({'get': 'retrieve'})),
    # path('/todos/update/<int:pk>', TodoViewSetCustom.as_view({'put': 'update'})),
    # path('/v2/todos', TodoViewSet.as_view())

    re_path('/v3/', include(api_v3)),
    re_path('/v4/', include(api_v4)),
    

]

urlpatterns += router.urls

