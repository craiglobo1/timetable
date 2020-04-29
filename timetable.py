class Timetable:
    def __init__(self,startTime = (7,30),endtime = (1,50)):
        self.startTime = startTime
        self.endTime = endtime
        self.schedule = []
        self.subjectList = ['physics','chemistry','biology','cs','business','accounts','economics','art','english','history','geography','math','it','pe']
        self.STUDENTLIMIT = 28
        self.studentsList = self.loadDataStudents()
        self.teachersList = self.loadDataTeachers()
        self.result = []
        self.students = []
        self.teachers = []

    def loadDataStudents(self):
        with open(r'F:\craigComp\Programming\python\timetable\Input Excel.csv','r') as rf:
            for line in rf:
                data = line.strip().lower()
                data = data.split(',')
                self.students.append(data)
        return self.students

    def loadDataTeachers(self):
        with open(r'F:\craigComp\Programming\python\timetable\teachers.csv','r') as rf:
            for line in rf:
                data = line.strip().lower()
                data = data.split(',')
                self.teachers.append(data)
        return self.teachers

    def getClassesForBlockTeacher(self,sub,blockNoI):
        for i in range(len(self.teachersList)):
            if self.teachersList[i][1] == sub and self.teachersList[i][blockNoI] < 29:
                self.counter +=1

            else:
                with open('ErrorReports.csv','a') as af:
                    af.write(self.teachersList[i][0])
    


    def printClassTeacher(self):
        run = True
        constant = len(self.studentsList)
        while run == True:
            for i in range(4):
                self.counter = 0
                for stud in range(constant):
                    for j in range(len(self.subjectList)):
                        if self.studentsList[stud][1] == self.subjectList[j]:
                            self.getClassesForBlockTeacher(self.subjectList[j],(i+2))
                            self.studentsList[stud].pop(1)
                 
            print ('List',self.totalLength())
            if self.totalLength() <= constant:
                run = False     
                print(self.studentsList)
                    
    def totalLength(self):
        totalLength = 0
        for student in self.studentsList:
            totalLength += len(student)
        return totalLength

    def collateClasses(self):
        return NotImplementedError

    def addPeriods(self,startTime,endTime,teacher,subject,students):
        return NotImplementedError
    
    def addRestrictionTime(self):
        return NotImplementedError
    
    def GetSchedule(self):
        return NotImplementedError
    
    def printSchedule(self):
        return NotImplementedError

time = Timetable()
print(time.printClassTeacher())

        