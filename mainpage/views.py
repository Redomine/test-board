from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post
from .forms import post_form



class show_main_page(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "main_page/post_list.html"


class show_post(DetailView):
    def get(self, request, pk):
        tred = Post.objects.get(id=pk)
        return render(request, "main_page/post_detail.html", {"tred": tred})


class AddPost(View):
    def post(self, request):

        form = post_form(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")