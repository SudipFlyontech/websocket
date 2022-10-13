# from django.conf.urls import include, url
from django import views
from django.urls import path
from django.contrib import admin
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('index/', views.index, name='index'),
    path('message/', views.MessageSendAPIView.as_view()),
    # path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    # path('user_list', user_list, name='user_list'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
