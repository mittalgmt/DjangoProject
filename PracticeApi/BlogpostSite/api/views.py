from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from .models import BlogPost
from rest_framework.views import APIView
# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self,request,*args,**kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


     
class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self,request,format=None):
        title = request.query_params.get("title","")

        if title:
            blog_post = BlogPost.objects.filter(title__icontains= title)
        else:
            blog_post = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_post,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
