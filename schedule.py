def schedule(sch1,bounds1,sch2,bounds2,duration):
    pointer1 = 0
    pointer2 = 0
    combinedSchedule = mergeArrays(sch1,sch2)
    if compareTime(bounds1[0],bounds2[0]) == -1:
        combinedSchedule.insert(0,['00:00',bounds1[0]])  
    else:
        combinedSchedule.insert(0,['00:00',bounds2[0]])

    if compareTime(bounds1[1],bounds2[1]) == 1:
        combinedSchedule.append([bounds1[1],'24:00'])  
    else:
        combinedSchedule.append([bounds2[1],'24:00'])
    print(combinedSchedule)

    i = 0
    while i < len(combinedSchedule)-1:
        start1 = combinedSchedule[i][0]
        end1 = combinedSchedule[i][1]
        start2 = combinedSchedule[i+1][0]
        end2 = combinedSchedule[i+1][1]
        if compareTime(end1,start2) in [1,0]:
            if compareTime(end2,end1) in [1,0]:
                TempEnd = end2
                combinedSchedule.pop(i+1)
                combinedSchedule[i][1] = TempEnd
                i-=1
            else:
                combinedSchedule.pop(i+1)
                i-=1
        i+=1
    i = 0
    output= []
    while i < len(combinedSchedule)-1:
        end1 = combinedSchedule[i][1]
        start2 = combinedSchedule[i+1][0]
        if timeDifference(end1,start2) >= duration:
            output.append([end1,start2])
        i+=1
    
    return output


def compareTime(time1,time2):
    time1 = time1.split(':')
    time2 = time2.split(':')
    min1 = int(time1[0])*60 + int(time1[1])
    min2 = int(time2[0])*60 + int(time2[1])
    if min1 > min2:
        return 1
    elif min1 < min2:
        return -1
    else:
        return 0
        
def timeDifference(time1,time2):
    time1 = time1.split(':')
    time2 = time2.split(':')
    min1 = int(time1[0])*60 + int(time1[1])
    min2 = int(time2[0])*60 + int(time2[1])
    return abs(min1-min2)

def mergeArrays(arr1, arr2): 
    arr3 = [None] * (len(arr1) + len(arr2)) 
    i = 0
    j = 0
    k = 0 
    while i < len(arr1) and j < len(arr2): 
        if compareTime(arr1[i][0],arr2[j][0]) == -1: 
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else: 
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < len(arr1): 
        arr3[k] = arr1[i]; 
        k = k + 1
        i = i + 1
   
    while j < len(arr2): 
        arr3[k] = arr2[j]; 
        k = k + 1
        j = j + 1
    return arr3

