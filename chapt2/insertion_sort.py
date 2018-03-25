import random
import time
from statistic import StatisticSort

def InsertionSort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key

def Test():
    n=100
    A=random.sample(range(n),n)
    print(A)
    startTime=time.time()
    InsertionSort(A)
    endTime=time.time()
    print(A)
    print(endTime-startTime)
    
def Bench():
    iterNum=100

    length1=100
    t1=StatisticSort(InsertionSort,iterNum,length1)

    length2=200
    t2=StatisticSort(InsertionSort,iterNum,length2)

    print("Iterating {} times every executing:\nFirst executing:\tlist size:{}\ttotal executing time:{}\nSecond executing:\tlist size:{}\ttotal executing time:{}\nRatio:{}".format(iterNum,length1,t1,length2,t2,t2/t1))

 
if __name__=="__main__":
    #Test()
    Bench()

