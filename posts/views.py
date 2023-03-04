from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

from django.http import Http404


# CRUD --> Create, Rertieve, Update, Delete
class PostListView(APIView): # we want send all post in api to client
    def get(self, request):  # use "GET" methode in this api
        posts = Post.objects.all()  # make query to get all post from database
        #posts = Post.objects.filter(is_enable=True) # wa can add some conditions for query
        serializer = PostSerializer(posts, many=True) # we have many object, so we should use "many=True" parameter in serializer
        return Response(serializer.data)  # methode 1: send serializer output to client, api responce is this
        # data = PostSerializer(posts, many=True) # methode 2: send serializer output to variable
        # return Response(serializer.data)    # send serializer output to client, api responce is this

    # we create a new post in database with the data that client send in body with POST methode
    def post(self, request): # use "POST" methode in this api
        serializer = PostSerializer(data=request.data)   # client data is in ".data", in other words ".data" is the body that we recieved from client in this api
        if serializer.is_valid():   # check based on the types that the recieved data is valid
            serializer.save()       # save new record in database
            return Response(serializer.data, status=status.HTTP_201_CREATED) # feedback the data that added to database and send "created" status to client
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # if the recieved data is not valid, we send "bad request" status to client
        #----- JSON format for create new post -----#
        # http://127.0.0.1:8000/posts/
        # {
        # "title": "api create post",
        # "text": "we using api to create this post",
        # "is_enable": true,
        # "publish_date": null
        # }


class PostDetailView(APIView): # we want send one post with its detail to client with api, for this purpose, we get id from client
    # when we get id or something like this,
    # we shoul use "try" to check the id number is exist in database and dont get 5xx error 
    # if the id number doesn't exist in database, we sen 404 error 
    def get_object(self, pk):   # this section uses many times in this class, so we defind this code and represent in one line
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        return post
    

    def get(self, request, pk): # use "GET" methode for getting available record in database
        # when we get id or something like this,
        # we shoul use "try" to check the id number is exist in database and dont get 5xx error 
        # if the id number doesn't exist in database, we sen 404 error 
    # method1 :
        # try:                         
        #     post = Post.objects.get(pk=pk)
        # except Post.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)   
    # method2 :
        post = self.get_object(pk)

        serializer = PostSerializer(post) # just on object, so we dont use "many=True" in this case
        return Response(serializer.data)  # send serializer output to client, api responce is this 
    # http://127.0.0.1:8000/posts/1/

    def put(self, request, pk): # use "PUT" methode for update available record in database 
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():   # check based on the types that the recieved data is valid
            serializer.save()       # update record in database
            return Response(serializer.data) # feedback the data that updated in database
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # if the recieved data is not valid, we send "bad request" status to client
    #----- JSON format for update available post -----#
    # {
    #     "title" : "this post updated with api",
    #     "text"  : "can change other fileds except id"
    # }


    def delete(self, request, pk):  # use "DELETE" methode for deleting available record in database 
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # feedback the data deleted in database and send, we send "no content" status to client