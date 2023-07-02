from .views import MovieViewSet, MovieInfoViewSet

from django.urls import path

urlpatterns = [
    path('movies', MovieViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('movies/<str:pk>', MovieViewSet.as_view({
        'get': 'retrieve',
        #'put': 'update',
        'put': 'addrating',
        'delete': 'remove'
    })),
    path('movieinfo', MovieInfoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('movieinfo/<str:pk>', MovieInfoViewSet.as_view({
        'post': 'create',
        'get': 'get',
        'put': 'update',
        'delete': 'remove',

    }))
]
