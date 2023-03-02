# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment 
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views import generic

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer

#------------ client to server : Method 1 ----------------#
#------------ http://127.0.0.1:8000/index/1/ -------------#
# @api_view(['GET','POST'])
# def index(request, pk):
#     #return HttpResponse('<h1>Welcome to Django<h1>')
#     print(request.data)
#     #return Response({'name': 'ALi Mohammadi'})  # it is dictionary
#     #return Response({'name': 'ALi Mohammadi'}, status=status.HTTP_400_BAD_REQUEST)  # it is dictionary
#     #return Response(dict(request.data))
#     try:
#         p = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response({'detail': 'Post not exits'}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer = PostSerializer(p)
#     print(serializer)
#     print('-' * 100)
#     print(serializer.data)
#     return Response(serializer.data)



#------------ client to server : Method 2 ----------------#
#------------ http://127.0.0.1:8000/index/?pk=1 -------------#
# @api_view(['GET','POST'])
# def index(request):
#     #return HttpResponse('<h1>Welcome to Django<h1>')
#     print(request.data)
#     #return Response({'name': 'ALi Mohammadi'})  # it is dictionary
#     #return Response({'name': 'ALi Mohammadi'}, status=status.HTTP_400_BAD_REQUEST)  # it is dictionary
#     #return Response(dict(request.data))
#     pk = request.query_params.get('pk')
#     print(request.query_params)
#     try:
#         p = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response({'detail': 'Post not exits'}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer = PostSerializer(p)
#     print(serializer)
#     print('-' * 100)
#     print(serializer.data)
#     return Response(serializer.data)



#------------ client to server : Method 3 ----------------#
@api_view(['GET','POST'])
def index(request):
    #return HttpResponse('<h1>Welcome to Django<h1>')
    print(request.data)
    #return Response({'name': 'ALi Mohammadi'})  # it is dictionary
    #return Response({'name': 'ALi Mohammadi'}, status=status.HTTP_400_BAD_REQUEST)  # it is dictionary
    #return Response(dict(request.data))
    pk = request.data.get('pk')
    print(request.data)

    try:
        p = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'detail': 'Post not exits'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(p)
    print(serializer)
    print('-' * 100)
    print(serializer.data)
    return Response(serializer.data)



def home(request):
    return HttpResponse('<h3>you are in home<h3>')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/post_list.html', context=context)

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


def post_detail(request, post_id):
#    try:
#        post = Post.objects.get(pk=post_id)
#    except Post.DoesNotExist:
#        return HttpResponseNotFound('Post is not exit!')

    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments':comments}
    return render(request, 'posts/post_detail.html', context=context)

class PostDetail(generic.DeleteView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        print(kwargs)
        context['comments'] = Comment.objects.filter(post =kwargs['object'].pk)
        return context



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts')
    else:
        form = PostForm()
    
    return render(request, 'posts/post_create.html', {'form': form})