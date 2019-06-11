from django.urls import path
from favorite_things import views

urlpatterns = [
    path('', views.Home.as_view(), name='index')
]