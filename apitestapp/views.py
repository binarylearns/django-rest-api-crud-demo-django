from rest_framework import generics
from .models import Posts
from .serializers import PostSerializers


# GET all posts + CREATE a post
class PostListing(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


# GET single post + UPDATE + DELETE
class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    lookup_field = "pk"
