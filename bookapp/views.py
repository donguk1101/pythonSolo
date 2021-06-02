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
    id = request.session['id']
    return  render(request,'main/home.html',{'session_id':id})

#Shop
def shop_main(request):
    id=request.session['id']
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
    return  render(request,'shop/shop_main.html',{"session_id":id,"totalpage":totalpage,"endpage":endpage,"startpage":startpage,"tablename":vTablename,'bookList':bl,"range":range(startpage,endpage+1)})

#MSG
def re_msg(request):
    msg=request.POST['msg']
    key=models.mainkey(models.komoran(msg))
    box={'key':str(key[0])}
    return  HttpResponse(json.dumps(box),content_type="application/json")
#basket
def basket(request):
    id=request.session['id']
    data=models.basket(id)
    list=[]
    for d in data:
        dd={"id":d[0],"poster":d[1],"title":d[2],"price":d[3],"ordercount":d[4],"realPrice":d[5],"no":d[6]}
        list.append(dd)

    return  render(request,'shop/basket.html',{'session_id':id,"list":list})

#join
def join(request):
    return  render(request,'member/join.html')
#우편번호
def postFind(request):
    key=request.POST['key']
    data=models.postFind(key)
    return  HttpResponse(json.dumps(data),content_type="application/json")
#login
def login_ok(request):
    return  render(request,'member/login.html',{'id':1})

def userLogin(request):
    id=request.POST['id']
    pwd=request.POST['pwd']
    db_id=models.member(id)
    if db_id == 0:
        return render(request,'member/login.html',{'id':0})
    db_pwd=models.member_pwd(id,pwd)
    if pwd !=db_pwd:
        return  render(request,'member/login.html',{'id':-1})
    request.session['id']=id
    return  redirect('home')
def sessionDelete(request):
    request.session['id'] = None
    return  redirect('home')
def basketAdd(request):
    list={}
    list[0]=request.POST['id']
    list[1] = request.POST['poster']
    list[2] = request.POST['title']
    list[3] = request.POST['price']
    list[4] = request.POST['ordercount']
    models.insertBasket(list)
    return HttpResponse("success",content_type="text")

def deleteBasket(request):
    no=request.POST['no']
    models.deleteBasket(int(no))
    return  HttpResponse("succsess",content_type="text")

def sign(request):
    list={}
    list[0]=request.POST['id']
    list[1] = request.POST['pwd1']
    list[2] = request.POST['name']
    list[3] = request.POST['birth']
    list[4]  = request.POST.get('code','')
    list[5] = request.POST.get('addr1','')
    list[6] = request.POST['addr2']
    list[7] = request.POST['tel']
    models.signUser(list)
    return  redirect('home')