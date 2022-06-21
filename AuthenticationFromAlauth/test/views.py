from allauth.account.views import login
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'test/index.html')
