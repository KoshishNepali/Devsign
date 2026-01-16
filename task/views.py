from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function based view(ui)
def index(request):
    return render(request,'task/index.html',{
        'title':'My first page',
        'description':'This is my first page description',
        'page_no':1
        
    })

def second_index(request):
    return render(request,'task/index2.html',{
        'name':'Koshish Pariyar',
        'course':'Python and django',
        'time_duration':2.5
    })
def third_index(request):
    return render(request,'task/index3.html',{
        'product_name':'baggy jeans',
        'price':3000,
        'pant_color':"darkblue"
    })