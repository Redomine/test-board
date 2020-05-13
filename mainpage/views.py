from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Posts


def show(request):
    return render(request, 'main_page/main_page.html')


class show_post(View):
    def get(self, request):
        treds = Posts.objects.all()
        return render(request, "main_page/main_page.html", {"tred_list": treds})