from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('Welcome to the Ledger App!')

def recipe_list(request):
    ctx = [
        
    ]


# Create your views here.
