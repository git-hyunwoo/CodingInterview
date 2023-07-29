def solution(num_list):
    answer = 0
    
    odd = ''
    even = ''
    for value in num_list:
        if value % 2 == 0:
            even += str(value)
        else:
            odd += str(value)
    
    answer = int(odd) + int(even)
    
    return answer