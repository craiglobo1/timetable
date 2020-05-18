from math import floor, ceil
from random import randint, choices, shuffle
from .settings import *


class period:
    def __init__(self, blockName, startTime, endTime):
        self.blockName = blockName
        self.startTime = startTime
        self.endTime = endTime


def periodSort(period):
    return period.startTime[0]*60 + period.startTime[1]


class Schedule:
    def __init__(self):
        self.schedule = [[] for i in range(noOfClassDays)]
        self.dayStartTime = (9, 00)
        self.dayEndTime = (16, 50)

    def calculateNoPeriods(self):
        return NotImplementedError

    def addPeriod(self, blockNo, day, startTime, endTime):
        self.schedule[day].append(period(blockNo, startTime, endTime))

    def addRestrictionTimeWeekly(self, restrictionName, day, startTime, endTime):
        self.schedule[day].append(period(restrictionName, startTime, endTime))
        schedule[day].sort(key=periodSort)

    def addRestrictionTimeDaily(self, restrictionName, startTime, endTime):
        for day in self.schedule:
            day.append(period(restrictionName, startTime, endTime))
            day.sort(key=periodSort)

    def addingLimits(self):
        self.addRestrictionTimeDaily('LowerBound', (0, 0), self.dayStartTime)
        self.addRestrictionTimeDaily('UpperBound', self.dayEndTime, (24, 0))

    def getFreePeriods(self, period1, period2):
        time1 = period1.endTime[0]*60 + period1.endTime[1]
        time2 = period2.startTime[0]*60 + period2.startTime[1]
        minDiff = time2 - time1
        periods = abs(minDiff/periodLength)
        return floor(periods)

    def addTime(self, time, extraTime):
        time = time[0]*60 + time[1]
        # extraTime = extraTime[0]*60 + extraTime[1]
        totalTime = time + extraTime
        totalTime = (floor(totalTime/60), totalTime % 60)
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
                periods = self.getFreePeriods(
                    self.schedule[i][j], self.schedule[i][j+1])
                # print(periods)
                durationPeriod = 0
                for z in range(periods):
                    newTime1 = self.addTime(
                        self.schedule[i][j].endTime, durationPeriod)
                    newTime2 = self.addTime(newTime1, periodLength)
                    self.schedule[i].append(period(1, newTime1, newTime2))
                    durationPeriod += periodLength
                    self.totalPeriodsWeek += 1
            self.schedule[i].sort(key=periodSort)

    def getBlockNumbers(self):
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

    def formatTime(self, time):
        minutes = time[0]*60 + time[1]
        return '{:02d}:{:02d}'.format(*divmod(minutes, 60))

    def displaySchedule(self):
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

    def runSchedule(self):

        self.addingLimits()
        break1Time = self.addTime((9, 00), periodLength*2)
        self.addRestrictionTimeDaily(
            'break', break1Time, self.addTime(break1Time, 30))
        break2Time = self.addTime((9, 00), periodLength*5+30)
        self.addRestrictionTimeDaily(
            'break', break2Time, self.addTime(break2Time, 90))
        self.GetSchedule()
        self.displaySchedule()
