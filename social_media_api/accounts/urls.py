from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegistrationView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view() , name='login'),
    path('register/', RegistrationView.as_view, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]