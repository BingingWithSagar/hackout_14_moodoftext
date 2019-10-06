from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)