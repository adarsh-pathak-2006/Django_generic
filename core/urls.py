from django.urls import path
from .views import *

urlpatterns=[
    path('', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('home', Home.as_view(), name='home'),
    path('home/<int:pk>/', Detail.as_view(), name='individual'),
    path('about/', About.as_view(), name='about'),
]