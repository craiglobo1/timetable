from math import floor,ceil
from random import randint,choices,shuffle

class Classes:
    def __init__(self,startTime = (7,30),endtime = (1,50)):
        self.startTime = startTime
        self.endTime = endtime
        self.schedule = []
        self.subjectList = ['physics','chemistry','biology','cs','business','accounts','economics','art','english','history','geography','math','it','pe']
        self.STUDENTLIMIT =  23
        self.studentsList = self.loadDataStudents()
        self.teachersList = self.loadDataTeachers()
        self.classes = []

    def loadDataStudents(self):
        students = []
        with open(r'databases\Subject Choices.csv','r',encoding='utf-8-sig') as rf:
            for line in  rf:
                data = line.strip().split(',')
                student = data[1][1:len(data[1])-1].strip().lower()
                subjects = [ subject.strip().lower() for subject in data[2][1:len(data[2])-1].split(';')]
                students.append([student,subjects])
        return students

    def loadDataTeachers(self):
        teachers = []
        with open(r'databases\teachers.csv', encoding='utf-8-sig',mode='r') as rf:
            for line in rf:
                data = line.strip().lower()
                data = data.split(',')
                teachers.append(data)
        return teachers
            
    def getClasses(self):
        classes = []
        for subject in self.subjectList:
            students = [ student[0] for student in self.studentsList if (subject in student[1]) ]
            clas = self.chunkIt(students)
            for i in range(len(clas)):
                try:
                    teacherIndex = [ teach[1] for teach in self.teachersList].index(subject)
                except: teacherIndex = None
                if teacherIndex:
                    teacher = self.teachersList[teacherIndex][0]
                    classes.append([teacher,subject,clas[i]])
                    self.teachersList.pop(teacherIndex)
                else: classes.append(['No Teacher',subject,clas[i]])
        self.classes = classes
        return classes

    def runClasses(self):
        return NotImplementedError

    def chunkIt(self,seq):
        shuffle(seq)
        sequenceLen = len(seq)
        limit = self.STUDENTLIMIT
        avgHigher = ceil(sequenceLen/limit)

        if avgHigher <= 1: return [seq]
        
        excess = sequenceLen % limit
        out = []

        if excess == 0:
            out = [seq[i:i+limit] for i in range(0, len(seq), limit)]
            return out
        else:
            out = [[ seq[i] for i in range(floor(sequenceLen/avgHigher))] for j in range(avgHigher-1)]

            count = (avgHigher-1)*floor(sequenceLen/avgHigher)

            temp=[]
            for i in range(sequenceLen-count):
                temp.append(seq[count])
                count +=1
            out.append(temp)
                    
            return out 

    
    def printClass(self):
        for line in self.classes:
            print(f'teacher: {line[0]}     subject: {line[1]}' + f'    length: {len(line[2])}' + ' \n' + 'students: ' +' ,'.join(line[2])+ '\n' )
            

time = Classes()
time.getClasses()
time.printClass()



class period:
    def __init__(self,blockName,startTime,endTime):
        self.blockName = blockName
        self.startTime = startTime
        self.endTime = endTime

def periodSort(period):
    return period.startTime[0]*60 + period.startTime[1]     

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


