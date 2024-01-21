def solution(my_string):
    answer = []
    # 65 ~ 90 : A ~ Z
    # 97 ~ 122 : a ~ z
    
    A_to_Z = range(65, 90 + 1)
    a_to_z = range(97, 122 + 1)
    
    for index in A_to_Z:
        count = my_string.count(chr(index))
        answer.append(count)
    
    for index in a_to_z:
        count = my_string.count(chr(index))
        answer.append(count)
    
    
    return answer