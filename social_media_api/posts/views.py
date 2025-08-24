from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(["GET"])
def feed(request):
    user = request.user
    following_users = user.following.all()  
    posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
    serializer = PostSerializer(posts, many=True)
    permissions.IsAuthenticated
    return Response(serializer.data)

permissions.IsAuthenticated, 
generics.get_object_or_404(Post, pk=pk), 
Like.objects.get_or_create(user=request.user, post=post), 
Notification.objects.create