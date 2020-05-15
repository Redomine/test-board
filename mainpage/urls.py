from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.show_post.as_view()),
    path("adding/", views.AddPost.as_view(), name="add_post")
]