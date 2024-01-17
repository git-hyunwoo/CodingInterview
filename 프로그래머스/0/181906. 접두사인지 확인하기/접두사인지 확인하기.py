def solution(my_string, is_prefix):
    answer = 0
    tmp = ""
    for character in my_string:
        tmp += character
        if tmp == is_prefix:
            answer = 1
    
    return answer