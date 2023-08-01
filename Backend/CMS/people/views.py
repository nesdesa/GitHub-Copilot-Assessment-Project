from django.shortcuts import render
from django.http import HttpResponse

def people(request):
    return HttpResponse("Hello, world. You're at the people index.")
