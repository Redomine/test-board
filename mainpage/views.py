from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Tred
from .forms import post_form
from .forms import comment_form



class show_main_page(ListView):
    model = Tred
    queryset = Tred.objects.all()
    template_name = "main_page/tred_list.html"


class show_tred(DetailView):
    model = Tred
    template_name = "main_page/tred_detail.html"



class AddTred(View):
    def post(self, request):
        form = post_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

class AddComment(View):
    def post(self, request, pk):
        form = comment_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.tred_parent_id = pk
            form.save()
        return redirect("/"+str(pk))