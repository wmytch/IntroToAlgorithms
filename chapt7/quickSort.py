import time
import random
import math
import sys
sys.path.append("..")
from tools.statistic import StatisticSort

def QuickSort(A,p,r):
    if p<r:
        #q=Partition(A,p,r)
        (q,t)=PartitionWithEqElement(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,t+1,r)

def RandomizedQuickSort(A,p,r):
    if p<r:
        q=RandomizedPartition(A,p,r)
        RandomizedQuickSort(A,p,q-1)
        RandomizedQuickSort(A,q+1,r)
def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            (A[i],A[j])=(A[j],A[i])
    (A[i+1],A[r])=(A[r],A[i+1])
    return i+1

def RandomizedPartition(A,p,r):
    i=random.randint(p,r)
    (A[i],A[r])=(A[r],A[i])
    return Partition(A,p,r)

def PartitionWithEqElement(A,p,r):
    x=A[r]
    i=p-1
    t=p-1
    for j in range(p,r):
        if A[j]<x :
            i+=1
            (A[i],A[j])=(A[j],A[i])
        elif A[j]==x:
            if t<i:
                t=i
            t+=1
            (A[t],A[j])=(A[j],A[t])
    (A[i+1],A[r])=(A[r],A[i+1])
    i+=1
    if t<i:
        t=i
    return (i,t)

def Test():
    n=10
    A=random.sample(range(n),n)
    print(A)
    startTime=time.time()
    QuickSort(A,0,len(A)-1)
    endTime=time.time()
    print(A)
    print(endTime-startTime)

def Bench():
    iterNum=100

    length1=100
    t1=StatisticSort(QuickSort,iterNum,length1,0,length1-1)
    
    length2=400
    t2=StatisticSort(QuickSort,iterNum,length2,0,length2-1)

    print("Iterating {} times every executing:\nFirst executing:\tlist size:{}\ttotal executing time:{}\nSecond executing:\tlist size:{}\ttotal executing time:{}\nRatio:{}".format(iterNum,length1,t1,length2,t2,t2/t1))


if __name__=="__main__":
    Test()
    #Bench()
 
