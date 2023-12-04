from django.shortcuts import render

from homeapp.models import art


# Create your views here.
def home (request):
    obj = art.objects.all()
    return render(request,'index.html',{'result':obj})