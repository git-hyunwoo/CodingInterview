def solution(a, b):
    answer = 0
    
    num_01 = int(str(a) + str(b))
    num_02 = 2 * a * b
    
    if num_01 > num_02:
        answer = num_01
    else:
        answer = num_02
    
    return answer