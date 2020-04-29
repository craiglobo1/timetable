from math import ceil
import random

class Poll:
    def __init__(self,noOfBlocks=4):
        self.noOfBlocks = noOfBlocks
        self.blockLimitPerSubject = 2
        self.studentLimit = 28
        self.popularStudentLimit = 4

    def getSubjectData(self):
        self.subjects = []
        self.students = []
        with open('Input Excel Poll.csv') as wf:
            for line in wf:
                data = line.split(',')
                data = [ info.strip().lower() for info in data]
                self.students.append(int(data[1]))
                self.subjects.append(data[0])

        return self.subjects


    def getClasses(self,studentLimit=28):
        STUDENTLIMIT = studentLimit
        classes = []
        totalClasses = 0

        for i in range(len(self.students)):
            if self.students[i]/STUDENTLIMIT != 0:
                noOfClasses = ceil(self.students[i]/STUDENTLIMIT)
                classes.append([self.subjects[i],noOfClasses])
                totalClasses += noOfClasses

        self.totalClasses = totalClasses
        self.classes = classes
        return classes
    
    def getClassesPerBlock(self):
        self.NoClassesPerBlock = self.chunkIt(self.totalClasses,self.noOfBlocks)
        return self.NoClassesPerBlock


    def popularity(self,students,subjects,number):
        self.studentSubjects = []

        for i in range(len(subjects)):
            self.studentSubjects.append([subjects[i],students[i]])
        # print(f'student Subjects:\n{self.studentSubjects}\n')

        def function(x):
            return x[1]

        self.studentSubjects.sort(reverse=True,key=function)
        self.popularList = [ self.studentSubjects[i][0] for i in range(number)]
        return self.popularList

    def getPopularClasses(self):
        self.popularClasses = []

        for i,clas in enumerate(self.classes):
            if clas[0] in self.popularList:
                self.popularClasses.append(clas)
        
        for i,clas in enumerate(self.classes):
            if clas[0] in self.popularList:
                self.classes.pop(i)

        # print(f'popular classes:\n{self.popularClasses}\n')

    def createBlockPopular(self):
        check = True
        popIndex = 0
        self.blocks = [ [] for i in range(self.noOfBlocks)]

        while check:
            for block in self.blocks:
                if not(self.popularClasses):
                    break

                block.append(self.popularClasses[popIndex][0])
                self.popularClasses[popIndex][1] -= 1

                if self.popularClasses[popIndex][1] == 0:
                    self.popularClasses.pop(popIndex)
                    
            if not(self.popularClasses):
                    check = False

    def removeClassesPopularAmt(self):
        for i in range(self.noOfBlocks):
            self.NoClassesPerBlock[i] -= len(self.blocks[i])

    def AddSujectsToBlocks(self):
        self.classes = [ clas for clas in self.classes  if clas[1] != 0 ]
        
        # print(f'classes:\n{self.classes}\n')

        for i,classlength in enumerate(self.NoClassesPerBlock):
            for j in range(classlength):
                index = random.randint(0,len(self.classes)-1)

                try:
                    if self.classes[index][1] == 0:
                        self.classes.pop(index)
                    currentClass = self.classes[index][0]
                except:
                    pass

                if self.blockLimitPerSubject == self.blocks[i].count(currentClass):
                    pass
                    pass

                try:
                    self.blocks[i].append(currentClass)
                    self.classes[index][1] -= 1
                except:
                    pass

                if not(self.classes):
                    break
            if not(self.classes):
                    break
    
    def getPollResult(self):
        self.getSubjectData()
        self.getClasses(self.studentLimit)
        self.getClassesPerBlock()
        self.popularity(self.students,self.subjects,self.popularStudentLimit)
        self.getPopularClasses()
        self.createBlockPopular()
        self.removeClassesPopularAmt()
        self.AddSujectsToBlocks()
        print(self.blocks)


    def chunkIt(self,num1,num2):
        seq = [ 0 for i in range(num1)]
        avg = len(seq) / float(num2)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return [ len(parts) for parts in out]

polls = Poll()
polls.getPollResult()