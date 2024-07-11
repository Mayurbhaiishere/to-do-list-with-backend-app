from django.http import HttpResponse
from django.shortcuts import render


def distraction(request):
    return render(request,'distraction_app/distraction.html')