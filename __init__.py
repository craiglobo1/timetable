from util.classes import Classes
from util.schdeule import Schedule
from util.poll import Poll


poll = Poll()
blocks = poll.runPoll()


classes = Classes(blocks)
classes.displayClasses()


time = Schedule()
time.runSchedule()
