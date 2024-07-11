from django.http import HttpResponse
from django.shortcuts import render

def to_do(request):
    return render(request,'to_do_app/to_do_here.html')

