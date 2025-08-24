from django.urls import path, include
from .views import PostViewStets, CommentViewStets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Post', PostViewStets)
router.register(r'Comment', CommentViewStets)

urlpatterns = [
    path('posts/', include(router.urls)),
]

urlpatterns = [
    path("feed/", views.feed, name="feed"),
]