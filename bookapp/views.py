from django.shortcuts import render
# Create your views here.
from .models import user
from django.views.generic import *
#메인
def index(request):
    return render(request,'main/index.html')
def home(request):
    return  render(request,'main/home.html')

#Shop
def shop_main(request):
    return  render(request,'shop/shop_main.html')


#join
def join(request):
    return  render(request,'admin/join.html')