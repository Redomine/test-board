from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.show_main_page.as_view()),
    path("add_comment/<int:pk>/", views.AddComment.as_view(), name="add_comment"),
    path("add_tred/", views.AddTred.as_view(), name="add_tred"),
    path("<int:pk>/", views.show_tred.as_view())
]