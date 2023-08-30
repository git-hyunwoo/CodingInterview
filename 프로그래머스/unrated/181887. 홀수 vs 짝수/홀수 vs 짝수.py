def solution(num_list):
    answer = 0
    
    odd = 0
    even = 0
    
    for index,value in enumerate(num_list):
        index += 1
        if index % 2 == 0:
            even += value
        else:
            odd += value
            
    if odd > even:
        answer = odd
    else:
        answer = even
    
    return answer