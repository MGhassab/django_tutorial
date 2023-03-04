from django.urls import path # in the past developers used url, but nowdays path is using

from .views import PostListView, PostDetailView # import view classes from views.py file
# we should include this file in urls.py in main project
urlpatterns = [                         # this is a list that contain api urls for this application
    path('',PostListView.as_view()),     # view in django is fuction base, PostListView is class, as_view() convert the class to fuction
    path('<int:pk>/', PostDetailView.as_view()) # in this api, we get id number from client in url (because using GET methode), "post_id" is name of this id number 
]