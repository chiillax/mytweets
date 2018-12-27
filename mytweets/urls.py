"""mytweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from tweets import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home.as_view(), name='home'),
    path('user/<str:userid>/', views.Profile.as_view(), name='username'),
    url(r'^user/(\w+)/post/$', views.PostTweet.as_view(), name='tweeter'),
    url(r'^hashtag/(\w+)/$', views.HashTagCloud.as_view(), name='hashtag'),
    url(r'^search/$', views.Search.as_view())
]
