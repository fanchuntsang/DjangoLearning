from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def search(request):
    return HttpResponse(request.POST['search'])
