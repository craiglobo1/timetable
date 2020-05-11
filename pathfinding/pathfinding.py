from util import *

class Poll:
    def __init__(self,noOfBlocks=4):
        self.noOfBlocks = noOfBlocks
        self.blockLimitPerSubject = 2
        self.studentLimit = 28
        self.popularStudentLimit = 4

    def getSubjectData(self):
        self.subjects = []
        self.students = []
        with open(r'F:\craigComp\Programming\python\timetable\databases\Input Excel Poll.csv') as wf:
    
            for line in wf:
                data = line.split(',')
                data = [ info.strip().lower() for info in data]
                self.students.append(int(data[1]))
                self.subjects.append(data[0])

        return self.subjects

    def shortestPath(self):
        InitialNode = Node(state=source,parent=None,action=None)
        frontier = QueueFrontier()

        frontier.add(InitialNode)
        explored = set()

poll = Poll()

print(poll.getSubjectData())