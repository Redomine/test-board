from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Post
from .forms import post_form



def show(request):
    return render(request, 'main_page/main_page.html')






class show_main_page(View):
    def get(self, request):
        treds = Post.objects.all()
        return render(request, "main_page/main_page.html", {"tred_list": treds})

class show_post(View):
    def get(self, request, key):
        tred = Post.objects.get(url=key)
        return render(request, "comment_section/comments.html", {"tred": tred})


class AddPost(View):
    def post(self, request):
        treds = Post.objects.all()
        for tred in treds:
            last_url = tred.url
        new_url = str(int(last_url)+1)

        form = post_form(request.POST)
        if form.is_valid():
            form.save()

        for tred in treds:
            print(tred.url)
        tred.url = new_url
        return redirect("/")