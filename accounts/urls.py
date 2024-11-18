from django.urls import path
from .views import *


urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('signout/', user_logout, name='user_logout'),
]