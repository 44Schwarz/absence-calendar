from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def calendar_view(request):
    return HttpResponse('There will be a calendar')
