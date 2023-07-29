def solution(n, control):
    answer = 0
    
    for direction in control:
        
        if direction == 'w':
            n += 1
        elif direction == 's':
            n += -1
        elif direction == 'd':
            n += 10
        elif direction == 'a':
            n += -10
        else:
            raise Exception("경고 : 입력은 w,s,d,a 범위 내에서만 가능합니다.")
    
    answer = n
    
    return answer