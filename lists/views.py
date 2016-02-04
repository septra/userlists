from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    html = "<html><head><title>To-Do</title></head><body><h1>To-Do</h1></body></html>"
    return HttpResponse(html)
