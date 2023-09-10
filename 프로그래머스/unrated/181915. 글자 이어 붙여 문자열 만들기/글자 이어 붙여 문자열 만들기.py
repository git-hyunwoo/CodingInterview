def solution(my_string, index_list):
    answer = ''
    for value in index_list:
        answer += my_string[value]
    return answer