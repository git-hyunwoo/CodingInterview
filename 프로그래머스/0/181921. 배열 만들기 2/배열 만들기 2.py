def solution(l, r):
    
    keys = [0,5]
    answer = []
    for value in range(l, r + 1):
        value = str(value)
        flag = True
        for v in value:
            v = int(v)
            if v not in keys:
                flag = False
                break
        if flag:
            answer.append(int(value))
            
    if len(answer) > 0:
        answer.sort()
    else:
        answer.append(-1)
    
    return answer