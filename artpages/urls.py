from django.urls import path
from .views import index, ArtListView, ArtDetailView, ArtListByTagView
from django.conf import settings
from django.conf.urls.static import static


# app_name = 'artists'
urlpatterns = [
    path('', index, name='index'),
    path('artworks/', ArtListView.as_view(), name='list_view'),
    path('artworks/tag/<str:tag>',ArtListByTagView.as_view(), name='tag_view'),
    path('artworks/<str:slug>', ArtDetailView.as_view(), name = 'detail_view')
]