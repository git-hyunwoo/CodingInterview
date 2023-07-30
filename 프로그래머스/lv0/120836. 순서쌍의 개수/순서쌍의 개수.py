def solution(n):
    answer = 0
    
    for value in range(1, n + 1):
        if n % value == 0:
            answer += 1
    
    return answer