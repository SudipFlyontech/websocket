from django.urls import path
from .consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/msg/<str:user>', ChatConsumer.as_asgi()),
]