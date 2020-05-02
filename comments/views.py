from django.shortcuts import render
from django.http import HttpResponse

#def show(request):
# #    return HttpResponse("Firs try")

def show(request):
    return render(request, 'comment_section/comments.html')