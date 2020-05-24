from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post
from .forms import post_form
from .forms import comment_form



class show_main_page(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "main_page/post_list.html"


class show_post(DetailView):
    model = Post
    template_name = "main_page/post_detail.html"



class AddPost(View):
    def post(self, request):
        form = post_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

class AddComment(View):
    def post(self, request, pk):

        return redirect("/")