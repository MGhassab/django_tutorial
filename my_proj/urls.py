"""my_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from posts.views import index, home, post_list, post_detail, post_create, PostList, PostDetail
urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('index/', index),
    path('home/', home),
    #path('posts/', post_list, name='post-list'),
    path('posts/', PostList.as_view()),
    #path('posts/<int:post_id>/', post_detail, name='post-detail'),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/create/', post_create)
]
