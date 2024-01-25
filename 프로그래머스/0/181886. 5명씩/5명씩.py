def solution(names):
    answer = []
    lst = [names[i:i + 5] for i in range(0,len(names),5)]
    for value in lst:
        answer.append(value[0])
        
    return answer