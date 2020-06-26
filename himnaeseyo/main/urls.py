
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card/create/', views.create, name='cardCreate'),
    path('card/save/', views.canvasToImage, name='cardImageSave'),
]
