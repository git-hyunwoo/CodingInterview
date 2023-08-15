def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        for value in num_list:
            answer += value
    else:
        answer = 1
        for value in num_list:
            answer *= value
            
    return answer