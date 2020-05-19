from math import floor
SUBJECTLIST = ['physics', 'chemistry', 'biology', 'computer science', 'business', 'accounting',
               'economics', 'art', 'english', 'history', 'mathematics',
                            'information technology', 'psychology', 'sociology', 'environmental']

STUDENTLIMIT = 24

noOfClassDays = 5
periodLength = 50
noOfBlocks = 4
weekdays = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wensday', 4: 'Thursday'}

def chunkIt(num1, num2):
    avgLower = floor(num1/num2)
    extraNum = num1 % num2
    out = []
    for i in range(num2):
        if extraNum != 0:
            extraNum -= 1
            out.append(avgLower+1)
        else:
            out.append(avgLower)
    return out

