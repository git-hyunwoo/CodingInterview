def solution(a, b):
    
    banswer = 0
    
    number_01 = int(str(a) + str(b))
    number_02 = int(str(b) + str(a))
    
    if number_01 > number_02:
        answer = number_01
    else:
        answer = number_02
    
    return answer