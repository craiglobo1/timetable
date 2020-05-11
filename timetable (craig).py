from math import floor
from random import randint,choices,shuffle
import pandas as pd

def periodSort(period):
    return period.startTime[0]*60 + period.startTime[1]

class period:
    def __init__(self,blockName,startTime,endTime):
        self.blockName = blockName
        self.startTime = startTime
        self.endTime = endTime
        

class schedule:
    def __init__(self):
        self.noOfClassDays = 5   
        self.periodLength = 40
        self.schedule = [ [] for i in range(self.noOfClassDays)]
        self.dayStartTime = (7,30)
        self.dayEndTime = (13,50)
        self.weekdays = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wensday',4:'Thursday'}
        self.noOfBlocks = 4

    def calculateNoPeriods(self):
        return NotImplementedError

    def addPeriod(self,blockNo,day,startTime,endTime):
        self.schedule[day].append(period(blockNo,startTime,endTime))
        
    def addRestrictionTimeWeekly(self,restrictionName,day,startTime,endTime):
        self.schedule[day].append(period(restrictionName,startTime,endTime))
        schedule[day].sort(key=periodSort)
        
    def addRestrictionTimeDaily(self,restrictionName,startTime,endTime):
        for day in self.schedule:
            day.append(period(restrictionName,startTime,endTime))
            day.sort(key=periodSort)
        
    def addingLimits(self):
        self.addRestrictionTimeDaily('LowerBound',(0,0),self.dayStartTime)
        self.addRestrictionTimeDaily('UpperBound',self.dayEndTime,(24,0))
            
    def getFreePeriods(self,period1,period2):
        time1 = period1.endTime[0]*60 + period1.endTime[1]
        time2 = period2.startTime[0]*60 + period2.startTime[1]
        minDiff = time2 -time1
        periods = abs(minDiff/self.periodLength)
        return floor(periods)

    def addTime(self,time,extraTime):
        time = time[0]*60 + time[1]
        # extraTime = extraTime[0]*60 + extraTime[1]
        totalTime = time + extraTime
        totalTime = (floor(totalTime/60),totalTime%60)
        if totalTime[0] >= 24:
            totalTime[0] -= 24
        return totalTime

    def GetSchedule(self):

        self.addPeriods()
        self.getBlockNumbers()

    def addPeriods(self):
        self.totalPeriodsWeek = 0
        for i in range(len(self.schedule)):
            for j in range(len(self.schedule[i])-1): 
                periods = self.getFreePeriods(self.schedule[i][j],self.schedule[i][j+1])
                # print(periods)
                durationPeriod = 0
                for z in range(periods):
                    newTime1 = self.addTime(self.schedule[i][j].endTime,durationPeriod)
                    newTime2 = self.addTime(newTime1,self.periodLength)
                    self.schedule[i].append(period(1,newTime1,newTime2))
                    durationPeriod += self.periodLength
                    self.totalPeriodsWeek += 1
            self.schedule[i].sort(key=periodSort)

            
    def getBlockNumbers(self):
        block = [0,1,2,3]
        self.blockLimit = self.chunkIt(self.totalPeriodsWeek,self.noOfBlocks)
        self.blockNo = [block[i] for i in range(len(self.blockLimit)) for j in range(self.blockLimit[i]) ]
        shuffle(self.blockNo) 
        counter = 0
        for day in self.schedule:
            for period in day:
                if period.blockName == 1:
                    period.blockName = self.blockNo[counter]+1
                    counter += 1
                
        

    def formatTime(self,time):
        hours,minutes = time
        if hours >= 10:
            hours = f'{hours}'
        else:
            hours = f'0{hours}'
        if minutes >= 10:
            minutes = f'{minutes}'
        else:
            minutes = f'0{minutes}'
        return f'{hours}:{minutes}'            
    
    def displaySchedule(self):
        for i,day in enumerate(self.schedule):
            print(f'\n{self.weekdays[i]}:\n')
            for j,period in enumerate(day):
                if type(period.blockName) == type(1):
                    print(f'block {period.blockName}   {self.formatTime(period.startTime)}   {self.formatTime(period.endTime)}')
                else:
                    print(f'{period.blockName}     {self.formatTime(period.startTime)}   {self.formatTime(period.endTime)}')
                pass
    def runSchedule(self):

        self.addingLimits()
        self.addRestrictionTimeDaily('break',(9,30),(9,50))
        self.addRestrictionTimeDaily('Class Teacher',(7,30),(8,10))
        self.GetSchedule()
        self.displaySchedule()

    
    def chunkIt(self,num1,num2):
        avgLower = floor(num1/num2)
        extraNum = num1%num2
        out = []
        for i in range(num2):
            if extraNum != 0:
                extraNum -= 1
                out.append(avgLower+1)
            else:
                out.append(avgLower)
        return out

timetable = schedule()
timetable.runSchedule()