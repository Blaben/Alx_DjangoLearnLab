from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(["POST"])
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    request.user.following.add(target_user)
    return Response({"message": f"You are now following {target_user.username}."})

@api_view(["POST"])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    request.user.following.remove(target_user)
    return Response({"message": f"You have unfollowed {target_user.username}."})
