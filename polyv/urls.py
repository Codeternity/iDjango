from django.urls import path

from . import views

urlpatterns = [
    path('player/', views.player, name='player'),
    path('', views.index, name='index')

]