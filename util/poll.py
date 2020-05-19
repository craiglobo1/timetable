from math import ceil, floor
from .parser import xlsxParser
from .settings import *



class Poll:
    parser = xlsxParser()

    def __init__(self):     # constructor and initializes the data from the database to the subjectChoices list
        self.subjectChoices = [[name[0].lower(), [name[i].lower() for i in [3, 4, 5, 6]]]
                               for name in self.parser.getDatabase('D7', 'J114', 'Sheet10')]

    def loadData(self):  # loads the data from the database and reformats it with the help of getStudentsInSubjectsmethod
        self.pollData = [[sub[0], len(sub[1])]
                         for sub in self.getStudentsInSubjects()]

    def sort(self):  # sorts the data in poll data based on popularity (total no Of students)
        def function(x):
            return x[1]

        self.pollData.sort(reverse=True, key=function)

    def getClasses(self):  # gets classes by dividing the noOfStudents by studentlimit and take ub and add those many of that subject to list
        self.pollData = [line[0] for line in self.pollData for _ in range(
            ceil(line[1]/STUDENTLIMIT))]

    def getBlocks(self):        #using the formatted data from getClasses method seprate the data in four blocks
        self.blocks = [[] for i in range(noOfBlocks)]
        counter = 0

        for i in range(noOfBlocks):

            for j in range(i, len(self.pollData), noOfBlocks):
                self.blocks[i].append(self.pollData[j].lower())

        return self.blocks

    def printBlocks(self):      #display the poll data
        for line in self.getBlocks():
            print(line)

    def getStudentsInSubjects(self):    #  reformat the subject choices list to StudentsInSubjects list
        studentsInSubjects = []
        for subject in SUBJECTLIST:
            studentsInSubject = []
            for student in self.subjectChoices:
                if subject in student[1]:
                    studentsInSubject.append(student[0])
            studentsInSubjects.append([subject, studentsInSubject])
        return studentsInSubjects

    def runPoll(self):  #encapsulation of the above methods in order
        self.loadData()
        self.sort()
        self.getClasses()
        return self.getBlocks()
