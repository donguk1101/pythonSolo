from django.urls import path
from bookapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name="home"),
    path('shop/',views.shop_main),
    path('join/',views.join),
    path('msg',views.re_msg,name="msg"),
    path('basket/',views.basket,name="basket"),
    path('join/postFind',views.postFind,name="postFind"),
    path('login_ok/',views.login_ok,name='login_ok'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('userLogout/',views.sessionDelete,name='userLogout'),
    path('shop/basketAdd',views.basketAdd),
    path('basket/deleteBasket',views.deleteBasket),
    path('join/sign',views.sign,name="sign"),


]