from .parser import xlsxParser
from math import floor
from random import shuffle
from .settings import *


class Classes:
    parser = xlsxParser()

    def __init__(self, blocks):
        self.blocks = blocks

        self.subjectChoices = [[name[0].lower(), [name[i].lower() for i in [3, 4, 5, 6]]]
                               for name in self.parser.getDatabase('D7', 'J114', 'Sheet10')]

        self.teachersList = [[item.lower() for item in teacher] for teacher in self.parser.getDatabase(
            'C5', 'D29', 'Teachers')]

        self.NoOfStudentsPerSubject = [
            [sub[0], len(sub[1])] for sub in self.getStudentsInSubjects()]

    def formatBlocks(self):
        for subject in SUBJECTLIST:
            NoOfSubject = 0
            for block in self.blocks:
                NoOfSubject += block.count(subject)

            for line in self.NoOfStudentsPerSubject:
                if line[0] == subject:
                    studentsInSubject = line[1]

            parts = chunkIt(studentsInSubject, NoOfSubject)
            counter = 0
            for i, block in enumerate(self.blocks):
                for j, subjects in enumerate(block):
                    if subjects == subject:
                        self.blocks[i][j] = [subjects, parts[counter]]
                        counter += 1
        # print(self.blocks)

    def teachAssignment(self):
        self.classes = self.blocks
        for i, block in enumerate(self.classes):
            tempTeachersList = self.teachersList[:]
            shuffle(tempTeachersList)
            for j, sub in enumerate(block):

                index = [teacher[1]
                         for teacher in tempTeachersList].index(sub[0])

                self.classes[i][j].insert(0, tempTeachersList[index][0])
                tempTeachersList.pop(index)
        # print(self.classes)

    def getStudentsInSubjects(self):
        studentsInSubjects = []
        for subject in SUBJECTLIST:
            studentsInSubject = []
            for student in self.subjectChoices:
                if subject in student[1]:
                    studentsInSubject.append(student[0])
            studentsInSubjects.append([subject, studentsInSubject])
        return studentsInSubjects

    def addStudents(self):
        StudentsInSubjects = self.getStudentsInSubjects()
        for i, block in enumerate(self.classes):
            for j, clas in enumerate(block):
                index = [item[0] for item in StudentsInSubjects].index(clas[1])
                students = StudentsInSubjects[index][1][:clas[2]]
                StudentsInSubjects[index][1] = StudentsInSubjects[index][1][clas[2]:]
                self.classes[i][j].append(students)
        return self.classes

    def getClasses(self):
        self.formatBlocks()
        self.teachAssignment()
        return self.addStudents()

    def displayClasses(self):
        for blockNo, block in enumerate(self.getClasses()):
            print(f'block {blockNo+1}: ', '\n')
            for clas in block:
                print(clas, '\n')