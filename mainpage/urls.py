from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.show_main_page.as_view()),
    path("add_post/", views.AddPost.as_view(), name="add_post"),
    path("<int:pk>/", views.show_post.as_view())
]