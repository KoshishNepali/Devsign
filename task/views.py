from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function based view(ui)
def index(request):
    return HttpResponse("Hello we are learning django")
def second_index(request):
    return HttpResponse("This is second page")