def closedPath(num):
    
    if (num == 0):
        return 1
    else:
        return closedPath_aux(num,0)

def closedPath_aux(num,closedPathCount):
                    #(0,1,2,3,4,5,6,7,8,9)
    closedPathValues=(1,0,0,0,1,0,1,1,2,1)
    
    if(num==0):
        return closedPathCount
    else:
        return closedPath_aux(num//10, closedPathCount+closedPathValues[num%10])


print(closedPath(630)) #---> 2
print(closedPath(1288)) #---> 4
