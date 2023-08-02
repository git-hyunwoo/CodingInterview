def solution(number):
    answer = 0
    
    if isOnlyNumber(number):
        answer = int(number) % 9
    
    return answer

def isOnlyNumber(number):
    
    # if parameter number contains only number between 0~9, return True
    # else return False
    
    flag = True
    
    for value in number:
        if int(value) not in range(0,9 + 1):
            flag = False
    
    return flag