def solution(n):
    answer = 0
    
    for z in range(1,n + 1):
        if z % 2 == 0:
            answer += z
    
    return answer