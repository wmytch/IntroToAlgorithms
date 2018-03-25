import time
import random

def StatisticSort(func,iterNum,length,*argList):
    totalTime=0
    for i in range(iterNum):
        unsortedList=random.sample(range(length),length)
        startTime=time.time()
        func(unsortedList,*argList)    
        endTime=time.time()
        totalTime+=endTime-startTime
    return totalTime

def StatisticSearch(func,iterNum,length,*argList):
    totalTime=0
    sortedList=[x for x in range(length)]
    for i in range(iterNum):
        seekNum=random.randrange(0,length-1)
        startTime=time.time()
        func(sortedList,seekNum,*argList)    
        endTime=time.time()
        totalTime+=endTime-startTime
    return totalTime
def StatisticFind(func,iterNum,length,*argList):
    totalTime=0
    for i in range(iterNum):
        unsortedList=random.sample(range(-length,length),length)
        startTime=time.time()
        func(unsortedList,*argList)    
        endTime=time.time()
        totalTime+=endTime-startTime
    return totalTime
        
