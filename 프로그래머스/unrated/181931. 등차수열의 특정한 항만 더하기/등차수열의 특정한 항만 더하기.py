def solution(a, d, included):
    answer = 0
    
    for index,value in enumerate(included):
        
        if value:
            answer += a
        
        a += d
    
    return answer