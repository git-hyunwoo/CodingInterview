def solution(my_string, alp):
    answer = ''
    for value in my_string:
        if value == alp:
            answer += alp.upper()
        else:
            answer += value
    return answer