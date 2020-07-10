
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('card/create/', views.create, name='cardCreate'),
    path('card/save/', views.cardImageSave, name='cardImageSave'),
]
