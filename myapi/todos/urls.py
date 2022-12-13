from django.urls import path
from rest_framework import routers


from .api import AllTodo, OneTodo, TodoViewSetCustom



router = routers.DefaultRouter()

router.register('/todos', TodoViewSetCustom, 'todosCustom')

urlpatterns = [

    path('/todos/all', AllTodo.as_view()),
    path('/todos/create', AllTodo.as_view()),
    path('/todos/one/<int:pk>', OneTodo.as_view()),
    # path('/todos/todos', TodoViewSetCustom.as_view({'get': 'list'})),
    path('/todos/todos', TodoViewSetCustom.as_view({'get': 'list'})),
    path('/todos/todos/<int:pk>', TodoViewSetCustom.as_view({'get': 'retrieve'})),
    path('/todos/update/<int:pk>', TodoViewSetCustom.as_view({'put': 'update'})),
]

urlpatterns += router.urls

