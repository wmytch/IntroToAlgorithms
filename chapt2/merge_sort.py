import time
import random
import math
from statistic import StatisticSort

def MergeSort(A,p,r):
    if p<r:
        q=(p+r)//2
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge1(A,p,q,r)

def Merge(A,p,q,r):
    B=A[p:q+1]
    C=A[q+1:r+1]
    B.append(math.inf)
    C.append(math.inf)
    i=j=0
    for k in range(p,r+1):
        if B[i]<=C[j]:
            A[k]=B[i]
            i+=1
        else :
            A[k]=C[j]
            j+=1

def Merge1(A,p,q,r):
    B=A[p:q+1]
    C=A[q+1:r+1]
    k=p
    i=j=0
    while i<len(B) and j<len(C):
        if B[i]<=C[j]:
            A[k]=B[i]
            i+=1
        else :
            A[k]=C[j]
            j+=1
        k+=1
    if i>=len(B):
        A[k:r+1]=C[j:len(C)]
    else:
        A[k:r+1]=B[i:len(B)]
def Test():
    n=100
    A=random.sample(range(n),n)
    print(A)
    startTime=time.time()
    MergeSort(A,0,n-1)
    endTime=time.time()
    print(A)
    print(endTime-startTime)
   

def Bench():
    iterNum=100

    length1=100
    t1=StatisticSort(MergeSort,iterNum,length1,0,length1-1)

    length2=800
    t2=StatisticSort(MergeSort,iterNum,length2,0,length2-1)

    print("Iterating {} times every executing:\nFirst executing:\tlist size:{}\ttotal executing time:{}\nSecond executing:\tlist size:{}\ttotal executing time:{}\nRatio:{}".format(iterNum,length1,t1,length2,t2,t2/t1))


if __name__=="__main__":
    Test()
    #Bench()
 
