from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('hello, World!!!')

def index(request):
    return render(request, 'users/index.html')

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'users/index.html')

def signup(request):
    return render(request, 'users/signup.html')
