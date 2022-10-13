
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django_ws.views import MessageSendAPIView,index
# from django.conf.urls import url
# from django_ws.views import login, logout signup, user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', MessageSendAPIView.as_view()),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('user_list', user_list, name='user_list'),
    path('index/', index),
    # path('login', login, name='login'),
    # path('logout', logout, name='logout'),
    # path('signup', signup, name='signup'),
]