import time
import random

class AlgorithmTools:

    def  __init__(self):
        self.totalTime=0

    def getSortedList(self,rangeStart,rangeEnd,step=1):
        return [x for x in range(rangeStart,rangeEnd,step)]

    def getUnSoredList(self,rangeStart,rangeEnd,length,step=1):
        return random.sample(range(rangeStart,rangeEnd,step),length)

    def getRandomNum(self,startNum,endNum):
        return random.randrange(startNum,endNum)

    def listSortTime(self,sortFunc,iterNum,length,*argList):
        for i in range(iterNum):
            unsortedList=self.getUnSortedList(0,length)
            startTime=time.time()
            sortFunc(unsortedList,*argList)    
            endTime=time.time()
            totalTime+=endTime-startTime
        return totalTime

    def listSearchTime(self,searchFunc,iterNum,length,*argList):
        sortedList=self.getSortedList(0,length)
        for i in range(iterNum):
            seekNum=self.getRandomNum(0,length-1)
            startTime=time.time()
            searchFunc(sortedList,seekNum,*argList)    
            endTime=time.time()
            totalTime+=endTime-startTime
        return totalTime

    def FindTime(self,func,iterNum,length,*argList):
        for i in range(iterNum):
            unsortedList=self.getUnSortedList(-length,length,length)
            startTime=time.time()
            func(unsortedList,*argList)    
            endTime=time.time()
            totalTime+=endTime-startTime
        return totalTime
        
