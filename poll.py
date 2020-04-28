import random
from math import ceil

def chunkIt(num1,num2):
    seq = [ 0 for i in range(num1)]
    avg = len(seq) / float(num2)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return [ len(parts) for parts in out]

def popularity(students,subjects,number):
    studentSubjects = []

    for i in range(len(subjects)):
        studentSubjects.append([subjects[i],students[i]])
    print(f'student Subjects:\n{studentSubjects}\n')

    def function(x):
        return x[1]

    studentSubjects.sort(reverse=True,key=function)
    return [ studentSubjects[i][0] for i in range(number)]



subjectList = []

students = []

with open('Input Excel Poll.csv') as wf:
    for line in wf:
        data = line.split(',')
        data = [ info.strip().lower() for info in data]
        students.append(int(data[1]))
        subjectList.append(data[0])


STUDENTLIMIT = 28
classes = []
totalClasses = 0

for i in range(len(students)):
    if students[i]/STUDENTLIMIT != 0:
        noOfClasses = ceil(students[i]/STUDENTLIMIT)
        classes.append([subjectList[i],noOfClasses])
        totalClasses += noOfClasses

print(f'Subject Class\n{classes}\n')

noOfBlocks = 4
blockLimitPerSubject = 2
classLimitPerSubject = 3

NoClassesPerBlock = chunkIt(totalClasses,noOfBlocks)

print(f'No of classes per block:\n{NoClassesPerBlock}\n')
blocks = []
block = []
            
popularityList = popularity(students,subjectList,4)
print(f'Popularity:\n{popularityList}\n')


popularClasses = 0
check = True
popIndex = 0

for clas in classes:
    if clas in popularityList:
        popularClasses += clas[1]


while check:
    for i in range(4):
        

    if popIndex == popularClasses:
        break
    popIndex += 1


for classlength in NoClassesPerBlock:
    for i in range(classlength):
        
        index = random.randint(0,len(classes)-1)
        currentClass = classes[index][0]

        if (currentClass in popularityList) and (1 == block.count(currentClass)):
            pass
            pass

        if blockLimitPerSubject == block.count(currentClass):
            pass
            pass

        block.append(currentClass)
        classes[index][1] -= 1

        if classes[index][1] == 0:
            classes.pop(index)

    blocks.append(block)
    block = []
    
print(f'Block:\n{blocks}\n')

