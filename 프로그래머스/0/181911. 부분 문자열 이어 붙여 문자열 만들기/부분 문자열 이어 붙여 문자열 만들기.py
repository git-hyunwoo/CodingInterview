def solution(my_strings, parts):
    answer = ''
    
    if len(my_strings) == len(parts):
        for i in range(0, len(my_strings)):
            start = parts[i][0]
            end = parts[i][1] + 1
            answer += my_strings[i][start : end]
        
    return answer