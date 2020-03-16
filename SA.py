import os.path
import pkgutil
import shutil
import sys
import struct
import tempfile
import math  
import copy
from decimal import *
import random

sys.setrecursionlimit(1000000)
def sort(a,b):  
    ans=[] 
    while len(a)!=0 and len(b)!=0 :
        if a[0]<b[0] :
            ans.append(a[0])
            a.remove(a[0])
        else :
            ans.append(b[0])
            b.remove(b[0])
    if len(a)==0 :
        ans=ans+b
    else :
        ans=ans+a
    #print("s",ans)
    return ans
def merge (num):
    if len(num)<=1 :
        return num
    mid=int(len(num)/2)
    a=num[0:mid]
    b=num[mid:]
    #print("m",a,b)
    return sort(merge(a),merge(b))

def findRoad(s) :
    global map
    n=0
    for i in range(0,len(s)-1) :
        n+=map[s[i]][s[i+1]]
    return n
            
loadFile = open("TSP.txt",'r')
Data=loadFile.readline()
Data=loadFile.readline()
global map
map=[]
a=[]
while len(Data)>=1 :   #設置數據
    Data=Data.replace('\t',' ')
    Data=Data.strip().split(' ')
    Data.remove(Data[0])
    #print(Data)
    for i in range(0,len(Data)) :
        a.append(int(Data[i]))
    map.append(a)
    a=[]
    Data=loadFile.readline()
#print(len(ans))
loadFile.close()
road=[]
for i in range(0,len(map[0])) :
    road.append(i)
print(road)
ans=findRoad(road)
#print(ans)
times=100000
#try :
#    times=int(input("how many times ? :"))
#except :
#    times=10000
p=0.5
counter=0 
print(ans)
bestroad=[]
bestans=10000
while counter<times :
    a=int(random.uniform(0,len(map)))
    b=int(random.uniform(0,len(map)))
    while b==a :
        b=int(random.uniform(0,len(map)))
    s=copy.deepcopy(road)
    c=s[a]
    s[a]=s[b]
    s[b]=c
    new=findRoad(s)
    if new<bestans :
        bestroad=copy.deepcopy(s)
        bestans=new
    if new<ans :
        ans=new
        road=copy.deepcopy(s)
    else :
        t=math.exp((ans-new)/ans)
        #print(t,"",end='')
        if t<p :
            ans=new
            #print("A",end='')
            road=copy.deepcopy(s)
    counter+=1
    #print(ans,"",end='')
print(bestroad)
print(bestans)
