import json

from django.db import models
import cx_Oracle, re
from konlpy.tag import Komoran

# Create your models here.

#회원
'''
class user(models.Model):
    user_id = models.CharField(max_length=34)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=34)
    tel = models.CharField(max_length=30)
    addr = models.TextField()
    email = models.CharField(max_length=50)
    birth = models.DateTimeField()

    def __str__(self):
        return self.user_id
'''
#shop

def getConnection():
    conn=""
    try:
        conn=cx_Oracle.connect("python1/0000@211.238.142.200:1521/XE")
    except Exception as e:
        print(e)
    return conn

#리스트
def bookList(page,tablename):
    conn=getConnection()
    cur=conn.cursor()
    rowSize=8
    page=int(page)
    start=1+(page-1)*rowSize
    end=rowSize*page
    sql=f"""
        SELECT no,title,subtitle,poster,author,company,price,'{tablename}',num
        FROM(SELECT no,title,subtitle,poster,author,company,price,'{tablename}',rownum as num
        FROM(SELECT no,title,subtitle,poster,author,company,price,'{tablename}'
        FROM {tablename} order by no asc))
        WHere num between {start} and {end}
            """
    cur.execute(sql)
    list=[]
    data=cur.fetchall()
    for d in data:
        list.append(d)
    cur.close()
    conn.close()
    return list
def bookTotalpage(tablename):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"SELECT Ceil(count(*)/8.0) from {tablename} "
    cur.execute(sql)
    total=cur.fetchone()
    cur.close()
    conn.close()
    return total[0]


def komoran(msg):
    komo = Komoran()
    arr=komo.nouns(msg)
    return arr
def secondKomoran(msg):
    komo = Komoran()
    arr=komo.pos(msg)
    print(arr)
    arr=komo.nouns(msg)
    print(arr)
    return  arr

def mainkey(key):
    conn=getConnection()
    cur=conn.cursor()
    list=[]
    for i in range(0,len(key)):
        try:
            sql=f"""
                    SELECT mainkey from chatbot_m
                    where mainkey = '{key[i]}' 
                """
            cur.execute(sql)
            data=cur.fetchone()
            if data == None:
                continue
            list.append(data[0])
        except Exception as e:
            continue
    cur.close()
    conn.close()
    if len(list) == 0:
        list.append(" ")
    return  list
def answer(msg):
    conn=getConnection()
    cur=conn.cursor()
    msg = re.sub('ㄴ', '노', msg)
    msg = re.sub('ㅇ', '넵', msg)
    msg=re.sub('[^가-힣]','',msg)
    sql=f"""
                SELECT result from answer 
                where answer='{msg}'
            """
    cur.execute(sql)
    data=cur.fetchone()
    cur.close()
    conn.close()
    result=""
    if data[0] == 1:
        result="주문 번호를 입력해주세요"
    elif data[0] == 0:
        result="최근 한 달간 주문내역을 조회하는 중입니다."
    return result
def answer2(msg):
    conn=getConnection()
    cur=conn.cursor()
    msg=re.sub('ㄴ','노',msg)
    msg = re.sub('ㅇ', '넵', msg)
    msg=re.sub('[^가-힣]','',msg)

    sql=f"""
                SELECT result from answer 
                where answer='{msg}'
            """
    cur.execute(sql)
    data=cur.fetchone()
    cur.close()
    conn.close()
    result=""
    if data[0] == 1:
        result="입력하신 주문번호로 환불접수하였습니다."
    elif data[0] == 0:
        result="다시 입력해주세요"
    return result
def subkey(msg,mainkey):
    conn=getConnection()
    cur=conn.cursor()
    for i in range(0,len(msg)):

        sql=f"""
            SELECT  result from chatbot_s
            WHERE subkey = '{msg[i]}' and mkey='{mainkey}'
            """
        print(sql)
        cur.execute(sql)
        data=cur.fetchone()
        print(data)
# 우편번호
def postFind(key):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
            select zipcode, sido||gugun||dong||bunji 
            from zipcode 
            where gugun like '%'||'{key}'||'%' or dong like '%'||'{key}'||'%'
            """
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data
def member(id):
    conn = getConnection()
    cur = conn.cursor()
    sql=f"""
            SELECT count(*) from member where id ='{id}'
        """
    cur.execute(sql)
    data=cur.fetchone()
    cur.close()
    conn.close()
    return data[0]
def member_pwd(id,pwd):
    conn = getConnection()
    cur = conn.cursor()
    sql = f"""
                SELECT pwd from member where id ='{id}'
            """
    cur.execute(sql)
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data[0]
def basket(id):
    conn =getConnection()
    cur=conn.cursor()
    sql=f"""
                SELECT id,poster,title,price,ordercount,to_number(price,'999999'),no,tb
                FROM basket 
                where id= '{id}'
                order by no desc
            """

    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return  data

def insertBasket(list):
    conn= getConnection()
    cur=conn.cursor()
    sql=f"""
            INSERT into basket Values( (SELECT NVL(max(no)+1,1) from basket),'{list[0]}','{list[1]}',
            '{list[2]}','{list[3]}',{list[4]},'{list[5]}' )    
    """
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def deleteBasket(no):
    conn =getConnection()
    cur=conn.cursor()
    sql=f"""
            DELETE from basket
            where no={no}
            """
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
def signUser(list):
    conn= getConnection()
    cur=conn.cursor()
    sql=f"""
            INSERT into member Values('{list[0]}','{list[1]}','{list[2]}',To_date('{list[3]}','YYYY-dd-MM' ),'{list[4]}',
            '{list[5]}','{list[6]}','{list[7]}','N'
             )    
    """
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def checkId(id):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
            SELECT count(*) from member
            WHERE id= '{id}' 
            """
    cur.execute(sql)
    data=cur.fetchone()
    cur.close()
    conn.close()
    return  data[0]
def findOrderNum(id):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
                SELECT no,title,poster,TO_CHAR(ordertime,'YY-mm-dd') ordertime
                from orderList
                where id='{id}' and (ordertime between SYSDATE-30 and SYSDATE)
                order by ordertime DESC
            """
    cur.execute(sql)
    list=[]
    data=cur.fetchall()
    for dd in data:
        box={"no":dd[0],"title":dd[1],"poster":dd[2],"ordertime":dd[3]}
        list.append(box)
    cur.close()
    conn.close()
    return list
def insertOrder(list,id):
    conn=getConnection()
    cur=conn.cursor()
    box=json.loads(list)
    for i in box:
        sql=f"""
            INSERT INTO orderList values(
            (SELECT NVL(max(no)+1,1) from orderList),'{id}',
            '{i["poster"]}','{i["title"]}','{i["price"]}',{i['ordercount']},SYSDATE
            ) 
            """
        cur.execute(sql)
        sql=f"""
            DELETE from basket 
            WHERE no={i['no']} and id='{id}'
            """
        cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def bestSeller():
    conn=getConnection()
    cur=conn.cursor()
    sql="""
        SELECT title,poster,num
            FROM (SELECT title,poster,rownum  num 
            FROM (SELECT title,max(poster) poster from orderlist
                GROUP by title
                order by count(title) ))
            where num between  1 and 10
                """
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data
def orderList(id,page):
    conn=getConnection()
    cur=conn.cursor()
    rowSize=10
    start=1+(page-1)*rowSize
    end=page*rowSize
    sql=f"""
        SELECT no,id,poster,title,price,ordercount,TO_char(ordertime,'yyyy-mm-dd') ordertime,(To_NUMBER(price,'99999')*ordercount) total,num
        from (SELECT no,id,poster,title,price,ordercount, ordertime,(To_NUMBER(price,'99999')*ordercount) total,rownum as num
        from (SELECT no,id,poster,title,price,ordercount,ordertime,(To_NUMBER(price,'99999')*ordercount) total 
        from orderlist order by ordertime DESC))
        where id='{id}' and num between {start} and {end}
        """
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data
def orderTotalpage(id):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""SELECT ceil(count(*)/10.0) from orderlist
            where id='{id}'
    """