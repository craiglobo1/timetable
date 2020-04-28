class Timetable:
    def __init__(self,startTime = (7,30),endtime = (1,50)):
        self.startTime = startTime
        self.endTime = endtime
        self.schedule = []
        self.subjectList = ['physics','chemistry','biology','cs','business','accounts','economics','art','english','history','geography']
        self.STUDENTLIMIT = 28

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
        teacherArr = self.loadDataTeachers()
        result = []
        for i in range(len(teacherArr)):
            if teacherArr[i][1] == 'cs':
                result.append(teacherArr[i][0])
                result.append(teacherArr[i][1])
        self.result = result
        return result

    def getClassesForBlockStudents(self,blockNo):
        studentsList = self.loadDataStudents()
        self.studentsList = [[data[0],data[blockNo]] for data in studentsList]
        self.result.append(studentsList)

    def printClassTeacher(self):
        run = True
        while run == True:
            self.result = []
            print(time.getClassesForBlockTeacher())
            for i in range(1,5):
                print(time.getClassesForBlockStudents(i))
            if self.studentsList == []:run=False

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
