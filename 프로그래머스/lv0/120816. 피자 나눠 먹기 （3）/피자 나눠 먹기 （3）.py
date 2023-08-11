def solution(slice, n):
    answer = 0
    while True:
        if answer >= n:
            break
        
        answer += slice
        
    answer = answer // slice
        
    return answer