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
        run = True
        constant = len(self.studentList)/4
        while run == True:
            for i in range(4):
                for stud in range(len(self.studentsList)):
                    if self.studentsList[stud][1] == 'math':
                        getClassesForBlockTeacher('math')
                        self.studentList[stud].pop(1)
                    
            if len(self.studentList) == constant:
                run = False     
                    


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
print(time.PrintClassTeacher())