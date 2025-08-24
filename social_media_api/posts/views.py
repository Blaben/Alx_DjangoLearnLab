from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(["GET"])
def feed(request):
    user = request.user
    following_users = user.following.all()  # assuming `following` is a ManyToMany field on CustomUser
    posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
