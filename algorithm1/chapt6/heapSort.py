import time
import random
import math
import sys
sys.path.append("..")
from tools.statistic import StatisticFind

def parent(i):
    if i %2 ==0:
        return (i-1)//2
    return i//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def maxHeapify(A,i,size):
    l=left(i)
    r=right(i)
    #print("({},{},{})".format(i,l,r))
    #if l<len(A) and r<len(A):
    #    print("(A[{}]={},A[{}]={},A[{}]={})".format(i,A[i],l,A[l],r,A[r]))
    if l<size and A[l]>A[i]:
        largest=l
    else:
        largest=i
    if r<size and A[r]>A[largest]:
        largest=r
    if largest!=i:
        (A[i],A[largest])=(A[largest],A[i])
        maxHeapify(A,largest,size)

def minHeapify(A,i,size):
    l=left(i)
    r=right(i)
    if l<size and A[l]<A[i]:
        smallest=l
    else:
        smallest=i
    if r<size and A[r]<A[smallest]:
        smallest=r
    if smallest!=i:
        (A[i],A[smallest])=(A[smallest],A[i])
        minHeapify(A,smallest,size)
def maxHeapifyByLoop(A,i):
    l=left(i)
    r=right(i)
    while l<len(A):
        if l<len(A) and A[l]>A[i]:
            largest=l
        else:
            largest=i
        if r<len(A) and A[r]>A[largest]:
            largest=r
        if largest!=i:
            (A[i],A[largest])=(A[largest],A[i])
            l=left(largest)
            r=right(largest)
            i=largest
        else:
            return
         

def buildMaxHeap(A):
    for i in range(len(A)//2,0,-1):
        maxHeapify(A,i-1,len(A));

def buildMinHeap(A):
    for i in range(len(A)//2,0,-1):
        minHeapify(A,i-1,len(A));

def heapSort(A):
    buildMaxHeap(A)
    size=len(A)
    for i in range(len(A)-1,0,-1):
        (A[0],A[i])=(A[i],A[0])
        size-=1
        maxHeapify(A,0,size) 

def heapMaximum(A):
    return A[0]

def heapExtractMax(A):
    assert len(A)>=1, "heap underflow"
    maxi=A[0]
    A[0]=A[len(A)-1]
    del A[len(A)-1]
    maxHeapify(A,0,len(A)-1)
    return maxi

def heapIncreaseKey(A,i,key):
    assert key> A[i] ,"new key is smaller than current key."
    A[i]=key
    while i>0 and A[parent(i)]<A[i]:
        (A[i],A[parent(i)])=(A[parent(i)],A[i])
        i=parent(i)

def maxHeapInsert(A,key):
    A.append(-math.inf)
    heapIncreaseKey(A,len(A)-1,key)


def heapMinimum(A):
    return A[0]

def heapExtractMin(A):
    assert len(A)>=1, "heap underflow"
    mini=A[0]
    A[0]=A[len(A)-1]
    del A[len(A)-1]
    minHeapify(A,0,len(A)-1)
    return mini

def heapDecreaseKey(A,i,key):
    assert key< A[i] ,"new key is bigger than current key."
   # A[i]=key
    while i>0 and A[parent(i)]>key:
       # (A[i],A[parent(i)])=(A[parent(i)],A[i])
        A[i]=A[parent(i)]
        i=parent(i)
    A[i]=key

def minHeapInsert(A,key):
    A.append(math.inf)
    heapDecreaseKey(A,len(A)-1,key)

def Test():
    n=10
    A=random.sample(range(n),n)
    print(A)
    startTime=time.time()
    buildMinHeap(A)
    print("优先队列:{}".format(A))
    print("最大值{}".format(heapMinimum(A)))
    mini=heapExtractMin(A)
    print("after heapExtractMin:{}-{}".format(A,mini))
    heapDecreaseKey(A,5,0)
    print("after heapIncreaseKey:{}".format(A))
    minHeapInsert(A,-1) 
    print("after maxHeapInsert:{}".format(A))
  #  heapSort(A)
    endTime=time.time()
    print(endTime-startTime)

def Bench():
    iterNum=100

    length1=100
    t1=StatisticFind(FindMaximumSubArray,iterNum,length1,0,length1-1)

    length2=300
    t2=StatisticFind(FindMaximumSubArray,iterNum,length2,0,length2-1)

    print("Iterating {} times every executing:\nFirst executing:\tlist size:{}\ttotal executing time:{}\nSecond executing:\tlist size:{}\ttotal executing time:{}\nRatio:{}".format(iterNum,length1,t1,length2,t2,t2/t1))


if __name__=="__main__":
    Test()
    #Bench()
 
