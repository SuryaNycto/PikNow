from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def customerpage(request):
    return render(request,'home.html')

def courierpage(request):
    return render(request,'home.html')