from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Tweet
from user_profile.models import User


def home(request):
    return render(request, 'base.html', {})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.filter(user=user)
    return render(request, 'profile.html', {'user':user, 'tweets':tweets})
