from django.db import models
import cx_Oracle
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
        SELECT no,title,subtitle,poster,author,company,price,num
        FROM(SELECT no,title,subtitle,poster,author,company,price,rownum as num
        FROM(SELECT no,title,subtitle,poster,author,company,price
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
def mainkey(key):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
            SELECT mainkey from chatbot_m
            where mainkey like '%'||'{key}'||'%' 
        """
    print(sql)
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return  data

arr=['택배배', '안와']
count=0
data=[]
for i in range(0,len(arr)):
    data.append(mainkey(arr[count]))
    count+=1

print(data)
print(len(data))