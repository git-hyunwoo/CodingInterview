def solution(s):
    
    if (len(s) == 4 or len(s) == 6) and isOnlyNumbers(s):
        return True
    else:
        return False        
    

def isOnlyNumbers(s):
    
    flag = True
    
    numbers = [str(x) for x in range(0,9 + 1)]
    
    for word in s:
        if word not in numbers:
            flag = False
        
    return flag
        