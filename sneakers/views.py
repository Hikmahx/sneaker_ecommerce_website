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
  # object_percentage = Sneaker.objects.all().annotate(difference=F('price') - F('discount_price'))
  print("this is working")
  # print(Sneaker.objects.all().defer('pk').values()) 
  print(Sneaker.objects.all().values()) 
  return render(request, 'home.html', {'sneakers' : sneakers})


def get_sneaker_details(request, product_id):
  sneaker = get_object_or_404(Sneaker, pk=product_id)
  return render(request, 'productpage.html', {'sneaker' : sneaker})


# def error_404(request):
#   data = {}
#         # return render(request,'home.html', data)
#   return HttpResponse("<h1>Hello there!!!</h1>")
