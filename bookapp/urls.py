from django.urls import path
from bookapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home),
    path('shop/',views.shop_main),
    path('join/',views.join),
]