from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.urls import reverse
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .models import Message
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import get_user_model, login, logout
# from django.contrib.auth.decorators import login_required

class MessageSendAPIView(APIView):
    # permission_classes = (IsAuthenticated)

    def get(self, request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("general", {"type": "send_info_to_user_group", "text": {"status": "done"}}
        )

        return Response({"status": True}, status=status.HTTP_200_OK)

    def post(self, request):
        user = 1
        msg = Message.objects.create(user_id=user, message={"message": request.data["message"]})
        socket_message = f"Message with id {msg.id} was created!"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"{user}-message", {"type": "send_last_message", "text": socket_message}
        )

        return Response({"status": True}, status=status.HTTP_201_CREATED)
    
def index(request):
    return render(request,"index.html")

# User = get_user_model()

# @login_required(login_url='/login/')
# def user_list(request):
#     """
#     NOTE: This is fine for demonstration purposes, but this should be
#     refactored before we deploy this app to production.
#     Imagine how 100,000 users logging in and out of our app would affect
#     the performance of this code!
#     """
#     users = User.objects.select_related('logged_in_user')
#     for user in users:
#         user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
#     return render(request, 'example/user_list.html', {'users': users})


# def login(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect(reverse('user_list'))
#         else:
#             print(form.errors)
#     return render(request, 'login.html', {'form': form})

# def signup(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('login'))
#         else:
#             print(form.errors)
#     return render(request, 'signup.html', {'form': form})


# def logout(request):
#     logout(request)
#     return redirect(reverse('login'))