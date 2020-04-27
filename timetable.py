

class Timetable:
    def __init__(self,startTime = (7,30),endtime = (1,50)):
        self.startTime = startTime
        self.endTime = endtime
        self.schedule = []


    def loadDataStudents(self):
        self.students = []
        with open('students.csv','r') as rf:
            for line in rf:
                data = line.strip()
                data = data.split(',')
                self.students.append(data)
        return self.students

    def loadDataTeachers(self):
        self.teachers = []
        with open('students.csv','r') as rf:
            for line in rf:
                data = line.strip()
                data = data.split(',')
                self.students.append(data)
        return self.teachers

    def GetSudents(self):
        return NotImplementedError

    def addPeriod(self,startTime,endTime,teacher,subject,students):
        return NotImplementedError
    
    def addRestrictionTime(self):
        return NotImplementedError
    
    def GetSchedule(self):
        return NotImplemented
    
    def printSchedule(self):
        return NotImplemented


time = Timetable()

print(time.loadData())

[(12,30),(1,50),'teacherName',['students...']]
