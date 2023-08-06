def solution(start, end):
    answer = []
    
    for value in range(start,end - 1,-1):
        answer.append(value)
    
    return answer