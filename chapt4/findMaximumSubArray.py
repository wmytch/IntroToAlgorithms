import time
import random
import math
import sys
sys.path.append("..")
from tools.statistic import StatisticFind

def FindMaximumSubArray(A,low,high):
    if high == low:
        return (low,high,A[low])
    else:
        mid=(low+high)//2
        (left_low,left_high,left_sum)=FindMaximumSubArray(A,low,mid)
        (right_low,right_high,right_sum)=FindMaximumSubArray(A,mid+1,high)
        (cross_low,cross_high,cross_sum)=FindMaxCrossingSubArray(A,low,mid,high)
    if left_sum>=right_sum and left_sum>=cross_sum:
        return (left_low,left_high,left_sum)
    elif right_sum>=left_sum and right_sum>=cross_sum:
        return (right_low,right_high,right_sum)
    else:
        return (cross_low,cross_high,cross_sum)

def FindMaxCrossingSubArray(A,low,mid,high):
    left_sum=-math.inf
    sum_value=0
    for i in range(mid,low-1,-1):
        sum_value=sum_value+A[i]
        if sum_value>left_sum:
            left_sum=sum_value
            max_left=i
    right_sum=-math.inf
    sum_value=0
    for j in range(mid+1,high+1):
        sum_value=sum_value+A[j]
        if sum_value>right_sum:
            right_sum=sum_value
            max_right=j
    return (max_left,max_right,left_sum+right_sum)
  
def ForceFindMaximumSubArray(A,low,high):
    max_sum=0
    for i in range(low,high+1):
        left_sum=-math.inf
        right_sum=-math.inf
        sum_value=0
        for j in range(i,low-1,-1):
            sum_value=sum_value+A[j]
            if sum_value>left_sum:
                left_sum=sum_value
                max_left=j
        sum_value=0
        for k in range(i+1,high+1):
            sum_value=sum_value+A[k]
            if sum_value>right_sum:
                right_sum=sum_value
                max_right=k
        if left_sum+right_sum >max_sum:
            max_sum=left_sum+right_sum
            left=max_left
            right=max_right   
    return (left,right,max_sum)

def Test():
    n=100
    A=random.sample(range(-n,n),n)
    print(A)
    startTime=time.time()
    (left,right,sum_value)=FindMaximumSubArray(A,0,n-1)
    endTime=time.time()
    print((left,right,sum_value))
    print(endTime-startTime)
    tmp=endTime-startTime
    print("force")
    startTime=time.time()
    (left,right,sum_value)=ForceFindMaximumSubArray(A,0,n-1)
    endTime=time.time()
    print((left,right,sum_value))
    print(endTime-startTime)
    print((endTime-startTime)/tmp)
   

def Bench():
    iterNum=100

    length1=100
    t1=StatisticFind(FindMaximumSubArray,iterNum,length1,0,length1-1)

    length2=300
    t2=StatisticFind(FindMaximumSubArray,iterNum,length2,0,length2-1)

    print("Iterating {} times every executing:\nFirst executing:\tlist size:{}\ttotal executing time:{}\nSecond executing:\tlist size:{}\ttotal executing time:{}\nRatio:{}".format(iterNum,length1,t1,length2,t2,t2/t1))


if __name__=="__main__":
    #Test()
    Bench()
 
