from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import View
from .models import Tweet, HashTag
from user_profile.models import User
from .form import TweetForm


def home(request):
    return render(request, 'base.html', {})


def profile(request, userid):
    user = get_object_or_404(User, username=userid)
    tweets = Tweet.objects.filter(user=user).order_by('-created_date')
    return render(request, 'profile.html', {'user': user, 'tweets': tweets})


def postTweet(request, userid):
    if request.method == "POST":
        user = User.objects.get(username=userid)
        text = request.POST.get('text')
        country = 'end'
        tweet = Tweet(text=text, user=user, country=country)
        tweet.save()
        words = text.split(" ")
        for word in words:
            if word[0] == "#":
                try:
                    hashtag = HashTag.objects.get(name=word[1:])
                except HashTag.DoesNotExist:
                    hashtag = HashTag(name=word[1:])
                    hashtag.save()
                hashtag.tweets.add(tweet)
                hashtag.save()
        return redirect('username', userid=user)
    # elif request.method == 'GET':
    #     profile(request, userid)
    #     user = get_object_or_404(User, username=userid)
    #     tweets = Tweet.objects.filter(user=user)
    #     # return render(request, 'profile.html', {'user': user, 'tweets': tweets})
