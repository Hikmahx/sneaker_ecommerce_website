from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Sneaker, SneakerImgs, Sizes, Color

# Create your views here.
def home(request):
  # return HttpResponse("<h1>Hello there!!!</h1>")
  return render(request, 'home.html')

# get all sneakers
def get_all_sneakers(request):
  sneakers= Sneaker.objects.all()
  print("this is working")
  return render(request, 'home.html', {'sneakers' : sneakers })