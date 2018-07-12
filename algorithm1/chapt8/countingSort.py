import time
import random
import math
import sys
sys.path.append("..")
from tools.statistic import StatisticSort
def randomList(randomRange,total):
    A=[]
    for i in range(0,total):
        A.append(random.randint(0,randomRange-1))
    return A;
def CountingSort(A,B,k):
    C=[0]*k
    for j in range(0,len(A)):
        C[A[j]]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]-=1
def Test():
    n=20
    k=10
    A=randomList(k,n)
    B=[0]*n
    print(A)
    startTime=time.time()
    CountingSort(A,B,k)
    endTime=time.time()
    print(B)
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
 
