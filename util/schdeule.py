from math import floor, ceil
from random import randint, choices, shuffle
from .settings import *


class period:   # period class to hold period values
    def __init__(self, blockName, startTime, endTime):
        self.blockName = blockName
        self.startTime = startTime
        self.endTime = endTime


def periodSort(period):  # to assist in sorting time
    return period.startTime[0]*60 + period.startTime[1]



class Schedule:
    # contructor and initializes all values
    def __init__(self, dayStartTime=(9, 00), dayEndTime=(16, 50)):
        self.schedule = [[] for i in range(noOfClassDays)]
        self.dayStartTime = dayStartTime
        self.dayEndTime = dayEndTime

    def addPeriod(self, blockNo, day, startTime, endTime):    # add a period class to schedule
        self.schedule[day].append(period(blockNo, startTime, endTime))

    # addition of non periods like pep once a week
    def addRestrictionTimeWeekly(self, restrictionName, day, startTime, endTime):
        self.schedule[day].append(period(restrictionName, startTime, endTime))
        schedule[day].sort(key=periodSort)

    # addition of non periods like break daily
    def addRestrictionTimeDaily(self, restrictionName, startTime, endTime):
        for day in self.schedule:
            day.append(period(restrictionName, startTime, endTime))
            day.sort(key=periodSort)

    def addingLimits(self):  # adding start and end times in a day
        self.addRestrictionTimeDaily('LowerBound', (0, 0), self.dayStartTime)
        self.addRestrictionTimeDaily('UpperBound', self.dayEndTime, (24, 0))

    # calculates no of free periods between restrictions
    def getFreePeriods(self, period1, period2):
        time1 = period1.endTime[0]*60 + period1.endTime[1]
        time2 = period2.startTime[0]*60 + period2.startTime[1]
        minDiff = time2 - time1
        periods = abs(minDiff/periodLength)
        return floor(periods)

    def addTime(self, time, extraTime):  # add time in minutes to a time like 12:00 + 30min = 12:30
        time = time[0]*60 + time[1]
        totalTime = time + extraTime
        totalTime = (floor(totalTime/60), totalTime % 60)
        if totalTime[0] >= 24:
            totalTime[0] -= 24
        return totalTime

    def GetSchedule(self):  # encapsulation of schedule

        self.addPeriods()
        self.getBlockNumbers()

    def addPeriods(self):       # an overcomplicated way to add periods between restrictions
        self.totalPeriodsWeek = 0

        # iterate on every day in schedule
        for i in range(len(self.schedule)):

            # iterate on every restriction(break, pep, etc) in a day
            for j in range(len(self.schedule[i])-1):
                periods = self.getFreePeriods(
                    self.schedule[i][j], self.schedule[i][j+1])     # calculate the no of periods that can fit between in restrictions

                durationPeriod = 0
                for z in range(periods):      # iterate on the free periods
                    newTime1 = self.addTime(
                        self.schedule[i][j].endTime, durationPeriod)    # start time of the period 
                    newTime2 = self.addTime(newTime1, periodLength)     # end time of the period
                    self.schedule[i].append(period(1, newTime1, newTime2))  #add a period
                    durationPeriod += periodLength          # increments the durationPeriod by period length so next period is exactly a period length away
                    self.totalPeriodsWeek += 1  
            self.schedule[i].sort(key=periodSort)  # sorts the schdule by period using periodsort defined above

    def getBlockNumbers(self):  # assign block numbers to periods
        block = [0, 1, 2, 3]
        self.blockLimit = chunkIt(self.totalPeriodsWeek, noOfBlocks)
        self.blockNo = [block[i] for i in range(
            len(self.blockLimit)) for j in range(self.blockLimit[i])]
        shuffle(self.blockNo)
        counter = 0
        for day in self.schedule:
            for period in day:
                if period.blockName == 1:
                    period.blockName = self.blockNo[counter]+1
                    counter += 1

    def formatTime(self, time):  # convert time in tuple to string
        minutes = time[0]*60 + time[1]
        return '{:02d}:{:02d}'.format(*divmod(minutes, 60))

    def displaySchedule(self):      # display the schedule visually in text
        for i, day in enumerate(self.schedule):
            print(f'\n{weekdays[i]}:\n')
            for j, period in enumerate(day):
                if type(period.blockName) == type(1):
                    print(
                        f'block {period.blockName}   {self.formatTime(period.startTime)}   {self.formatTime(period.endTime)}')
                else:
                    print(
                        f'{period.blockName}     {self.formatTime(period.startTime)}   {self.formatTime(period.endTime)}')
                pass

    def runSchedule(self):      # adding limits and constriction and running the program
        self.addingLimits()
        break1Time = self.addTime((9, 00), periodLength*2)
        self.addRestrictionTimeDaily(
            'break', break1Time, self.addTime(break1Time, 30))
        break2Time = self.addTime((9, 00), periodLength*5+30)
        self.addRestrictionTimeDaily(
            'break', break2Time, self.addTime(break2Time, 90))
        self.GetSchedule()
        self.displaySchedule()
