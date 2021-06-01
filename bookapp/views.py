import json

from django.http import HttpResponse
from django.shortcuts import render,redirect
from bookapp import models
import  re
# Create your views here.
#from .models import user
from django.views.generic import *
#메인
def index(request):
    return render(request,'main/index.html')
def home(request):
    return  render(request,'main/home.html')

#Shop
def shop_main(request):
    try:
        page=request.GET['page']
    except:
        page=1
    vTablename=request.GET['tb']
    tablename='A'+str(re.sub('[/()-· ]','',vTablename))[0:6]
    curpage=int(page)
    block=10
    startpage=int((curpage-1)/block)*block+1
    endpage=int((curpage-1)/block)*block+10
    totalpage=models.bookTotalpage(tablename)
    if endpage>=totalpage:
        endpage=totalpage
    bookList=models.bookList(curpage,tablename)
    bl=[]
    for b in bookList:
        bb={"no":b[0],"title":b[1],"subtitle":b[2],"poster":b[3],"author":b[4],"company":b[5],"price":b[6]}
        bl.append(bb)
    return  render(request,'shop/shop_main.html',{"totalpage":totalpage,"endpage":endpage,"startpage":startpage,"tablename":vTablename,'bookList':bl,"range":range(startpage,endpage+1)})

#MSG
def re_msg(request):
    msg=request.POST['msg']
    key=models.mainkey(models.komoran(msg))
    box={'key':str(key[0])}
    return  HttpResponse(json.dumps(box),content_type="application/json")
#basket
def basket(request):
    return  render(request,'shop/basket.html')

#join
def join(request):
    return  render(request,'admin/join.html')