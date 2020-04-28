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


    def getClassesForBlockTeacher(self):
        self.result.append(self.teachersList[i][0])
        self.result.append(self.teachersList[i][1])

    def getClassesForBlockStudents(self):
        return NotImplementedError
        
    def PrintClassTeacher(self):
        run = True
        while run == True:
            getClassesForBlockTeacher()
            for i in range(4):
                pass

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
time.PrintClassTeacher()