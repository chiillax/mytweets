from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from django.views.generic import View
from .models import Tweet, HashTag
from user_profile.models import User
from .form import TweetForm, SearchForm
from django.template.loader import render_to_string
from django.template import Context
import json


class Home(View):
    def get(self, request):
        tweets = Tweet.objects.all().order_by('-created_date')
        return render(request, 'home.html', {'tweets': tweets})


class Profile(View):
    def get(self, request, userid):
        user = get_object_or_404(User, username=userid)
        tweets = Tweet.objects.filter(user=user).order_by('-created_date')
        tweetform = TweetForm()
        return render(request, 'profile.html', {'user': user, 'tweets': tweets, 'tweetform': tweetform})


# class PostTweet(View):
#     def post(self, request, userid):
#         # if request.method == "POST":
#         user = User.objects.get(username=userid)
#         text = request.POST.get('text')
#         country = 'end'
#         tweet = Tweet(text=text, user=user, country=country)
#         tweet.save()
#         words = text.split(" ")
#         for word in words:
#             if word[0] == "#":
#                 try:
#                     hashtag = HashTag.objects.get(name=word[1:])
#                 except HashTag.DoesNotExist:
#                     hashtag = HashTag(name=word[1:])
#                     hashtag.save()
#                 hashtag.tweets.add(tweet)
#                 hashtag.save()
#         return redirect('username', userid=user)


class PostTweet(View):
    def post(self, request, username):
        # form = TweetForm(self.request.POST)
        # if form.is_valid():
        user = User.objects.get(username=username)
        text = request.POST.get('text')
        tweet = Tweet(text=text, user=user,country=request.POST.get('csrfmiddlewaretoken'))
        tweet.save()
        words = text.split(" ")
        for word in words:
            if word[0] == "#":
                hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                hashtag.tweets.add(tweet)
        # return HttpResponseRedirect('/user/'+username)
        return redirect('username', userid=user)


class HashTagCloud(View):
    def get(self, request, hashtag):
        tweets = HashTag.objects.get(name=hashtag).tweets.all()
        return render(request, 'hashtag.html', {'tweets': tweets})


class Search(View):
    def get(self, request):
        searchform = SearchForm()
        return render(request, 'search.html', {'searchform': searchform})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets = Tweet.objects.filter(text__icontains=query)
            return_str = render_to_string('partials/_tweet_search.html', {'query':query, 'tweets':tweets})
            return HttpResponse(json.dumps(return_str), content_type="application/json")
        else:
            HttpResponseRedirect("/search")
