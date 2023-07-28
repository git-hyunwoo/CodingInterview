def solution(num_list):
    answer = 0
    for index,value in enumerate(num_list):
        if value < 0:
            answer = index
            break
        else:
            answer = -1
    return answer