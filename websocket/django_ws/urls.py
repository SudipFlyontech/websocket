# from django.conf.urls import include, url
from django import views
from django.urls import path
from django.contrib import admin
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('index/', views.index, name='index'),
    path('message/', views.MessageSendAPIView.as_view()),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.UserLogin, name='login'),
    path('logout', views.UserLogout, name='logout'),
    path('user_list', views.User_List, name='user_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
