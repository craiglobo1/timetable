from math import floor
class Timetable:
    def __init__(self,startTime = (7,30),endtime = (1,50)):
        self.startTime = startTime
        self.endTime = endtime
        self.schedule = []
        self.subjectList = ['physics','chemistry','biology','cs','business','accounts','economics','art','english','history','geography']
        self.STUDENTLIMIT = 28
        self.studentsList = self.loadDataStudents()
        self.teachersList = self.loadDataTeachers()
        self.result = []

    def loadDataStudents(self):
        self.students = []
        with open(r'F:\craigComp\Programming\python\timetable\Input Excel.csv','r') as rf:
            for line in rf:
                data = line.strip()
                data = data.split(',')
                self.students.append(data)
        return self.students

    def loadDataTeachers(self):
        self.teachers = []
        with open(r'F:\craigComp\Programming\python\timetable\teachers.csv','r') as rf:
            for line in rf:
                data = line.strip()
                data = data.split(',')
                self.teachers.append(data)
        return self.teachers

    

    def getClassesForBlockTeacher(self,sub):
        for i in range(len(self.teachersList)):
            if self.teacherList[i][1] == sub and self.teacherList[i][2] < 29:
                self.teacherList[i][2] = self.teacherList[i][2] + 1
            else:
                with open('ErrorReports.csv','a') as af:
                    af.append(self.teacherList[i][1])
        
    def PrintClassTeacher(self):
        return NotImplementedError


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
        self.blockLimit = 15
        self.periodLength = 40
        self.schedule = [ [] for i in range(self.noOfClassDays)]
        self.dayStartTime = (7,30)
        self.dayEndTime = (13,50)

    def calculateNoPeriods(self):
        return NotImplementedError

    def addPeriod(self,blockNo,day,startTime,endTime):
        self.schedule[day].append(period(blockNo,startTime,endTime))
        
    def addRestrictionTimeWeekly(self,restrictionName,day,startTime,endTime):
        self.schedule[day].append(period(restrictionName,startTime,endTime))
        
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
            self.schedule[i].sort(key=periodSort)
                
                

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
            print(f'Day {i+1}:')
            for period in day:
                print(f'{period.blockName}   {self.formatTime(period.startTime)}   {self.formatTime(period.endTime)}')

timetable = schedule()
timetable.addingLimits()
timetable.addRestrictionTimeDaily('break',(9,30),(9,50))
timetable.GetSchedule()
timetable.displaySchedule()
