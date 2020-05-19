from .parser import xlsxParser
from math import floor
from random import shuffle
from .settings import *


class Classes:
    parser = xlsxParser()

    def __init__(self, blocks): #constructor and intializing the data from the database
        self.blocks = blocks

        self.subjectChoices = [[name[0].lower(), [name[i].lower() for i in [3, 4, 5, 6]]]
                               for name in self.parser.getDatabase('D7', 'J114', 'Sheet10')]

        self.teachersList = [[item.lower() for item in teacher] for teacher in self.parser.getDatabase(
            'C5', 'D29', 'Teachers')]

        self.NoOfStudentsPerSubject = [
            [sub[0], len(sub[1])] for sub in self.getStudentsInSubjects()]

    def addNoOfStudents(self):
        for subject in SUBJECTLIST:
            NoOfSubject = 0  # counter for total students for each subject
            for block in self.blocks:
                NoOfSubject += block.count(subject)

            for line in self.NoOfStudentsPerSubject:  # find students taking each subject and store in studentsInSubject
                if line[0] == subject:
                    studentsInSubject = line[1]

            parts = chunkIt(studentsInSubject, NoOfSubject)
            counter = 0
            for i, block in enumerate(self.blocks):             # add students
                for j, subjects in enumerate(block):
                    if subjects == subject:
                        self.blocks[i][j] = [subjects, parts[counter]]
                        counter += 1

    def teachAssignment(self):
        self.classes = self.blocks
        # go through every block in classes
        for i, block in enumerate(self.classes):
            tempTeachersList = self.teachersList[:]
            shuffle(tempTeachersList)
            for j, sub in enumerate(block):  # go through every subject in the block

                index = [teacher[1]  # find the index of the subject in the tempTeachersList
                         for teacher in tempTeachersList].index(sub[0])

                # insert the teacher from tempTeachersList to classes
                self.classes[i][j].insert(0, tempTeachersList[index][0])


                # remove that teacher from the tempTeachersList
                tempTeachersList.pop(index)


    def getStudentsInSubjects(self):            # create a Students In each Subject list from Subject choices of students
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
        for i, block in enumerate(self.classes):                        #adding students in each class 
            for j, clas in enumerate(block):
                index = [item[0] for item in StudentsInSubjects].index(clas[1])
                students = StudentsInSubjects[index][1][:clas[2]]
                StudentsInSubjects[index][1] = StudentsInSubjects[index][1][clas[2]:]
                self.classes[i][j].append(students)
        return self.classes

    def getClasses(self):           # encapsulation of all the methods from above
        self.addNoOfStudents()
        self.teachAssignment()
        return self.addStudents()

    def displayClasses(self):               #print the classes list in a visually nice way
        for blockNo, block in enumerate(self.getClasses()):
            print(f'block {blockNo+1}: ', '\n')
            for clas in block:
                print(clas, '\n')
