from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.show_main_page.as_view()),
    path("adding/", views.AddPost.as_view(), name="add_post"),
    path("<int:key>/", views.show_post.as_view())
]