def solution(num_list):
    answer = 0 
    
    sum_pow_element = 0
    mul_element = 1
    
    for value in num_list:
        sum_pow_element += value
        mul_element *= value    
            
    print(f'pow(sum_pow_element,2) : {pow(sum_pow_element,2)}')
    print(f'mul_element : {mul_element}')
    if pow(sum_pow_element,2) > mul_element:
        answer = 1
    
    return answer