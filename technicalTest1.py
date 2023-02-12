"""
This recursive function counts all the digits of closed paths that could contain 
a number.

    I: num::int
    O: closedPathCount::int
"""
def closedPath(num):
    
    if (num == 0):
        return 1
    else:
        return closedPath_aux(num,0)

"""
This is an helper recursive function, it helps to add a new parameter to 
manage the closed paths counter.
    I: num::int, closedPathCount
    O: closedPathCount:: int
"""
def closedPath_aux(num,closedPathCount):
                    #(0,1,2,3,4,5,6,7,8,9)
    closedPathValues=(1,0,0,0,1,0,1,0,2,1)
    
    if(num==0):
        return closedPathCount
    else:
        return closedPath_aux(num//10, closedPathCount+closedPathValues[num%10])


""" 
Those lines displays the result of closedPath function.
"""
print(closedPath(630)) #---> 2
print(closedPath(1288)) #---> 4
