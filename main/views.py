from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainView(request):
    return HttpResponse("Hello Everyone")


#Main Dashboard
def dashboard(request):
    return render(request, 'main/base.html')


    
    