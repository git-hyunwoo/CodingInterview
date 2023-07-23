def solution(angle):
    answer = 0
    
    # 0~89 : 예각
    # 90 : 직각
    # 91~179 : 둔각
    # 180 : 평각
    
    if angle >= 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle >= 90 and angle < 180:
        answer = 3
    elif angle >= 180:
        answer = 4
    
    return answer