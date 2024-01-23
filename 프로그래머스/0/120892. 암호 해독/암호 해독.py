def solution(cipher, code):
    answer = ''
    
    for index, value in enumerate(cipher):
        index += 1
        if index % code == 0:
            answer += value
    
    return answer