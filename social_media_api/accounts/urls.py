from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegistrationView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view() , name='login'),
    path('register/', RegistrationView.as_view, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile, name="profile"),
]

path("follow/<int:user_id>/", views.follow_user, name="follow_user"),
path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow_user"),