from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Posts
from .forms import post_form



def show(request):
    return render(request, 'main_page/main_page.html')


class show_post(View):
    def get(self, request):
        treds = Posts.objects.all()
        return render(request, "main_page/main_page.html", {"tred_list": treds})

class AddPost(View):
    def post(self, request):
        form = post_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")