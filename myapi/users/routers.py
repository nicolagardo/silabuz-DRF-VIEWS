from rest_framework.routers import Route, SimpleRouter, DefaultRouter
from rest_framework import routers


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
        )
    ]
