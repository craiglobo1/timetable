from util.classes import Classes
from util.schdeule import Schedule
from util.poll import Poll
import pygame


poll = Poll()
blocks = poll.runPoll()
classes = Classes(blocks)
clas = classes.getClasses()
