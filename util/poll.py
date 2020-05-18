from math import ceil, floor
from .parser import xlsxParser
from .settings import *


class Poll:
    parser = xlsxParser()

    def __init__(self):

        self.subjectChoices = [[name[0].lower(), [name[i].lower() for i in [3, 4, 5, 6]]]
                               for name in self.parser.getDatabase('D7', 'J114', 'Sheet10')]

    def loadData(self):
        self.pollData = [[sub[0], len(sub[1])]
                         for sub in self.getStudentsInSubjects()]

    def sort(self):
        def function(x):
            return x[1]

        self.pollData.sort(reverse=True, key=function)

    def getClasses(self):
        self.pollData = [line[0] for line in self.pollData for _ in range(
            ceil(line[1]/STUDENTLIMIT))]

    def getBlocks(self):
        self.blocks = [[] for i in range(noOfBlocks)]
        counter = 0

        for i in range(noOfBlocks):

            for j in range(i, len(self.pollData), noOfBlocks):
                self.blocks[i].append(self.pollData[j].lower())

        return self.blocks

    def printBlocks(self):
        for line in self.getBlocks():
            print(line)

    def getStudentsInSubjects(self):
        studentsInSubjects = []
        for subject in SUBJECTLIST:
            studentsInSubject = []
            for student in self.subjectChoices:
                if subject in student[1]:
                    studentsInSubject.append(student[0])
            studentsInSubjects.append([subject, studentsInSubject])
        return studentsInSubjects

    def runPoll(self):
        self.loadData()
        self.sort()
        self.getClasses()
        return self.getBlocks()
