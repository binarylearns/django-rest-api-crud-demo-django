from django.urls import path
from .import views

urlpatterns = [
    path(
        "blogpost/",
        views.PostListing.as_view(),
        name="blogpost_view_create"
    ),


  path(
      "blogpost/<int:pk>/",
      views.PostUpdate.as_view(),
      name="update"
  ),
]
