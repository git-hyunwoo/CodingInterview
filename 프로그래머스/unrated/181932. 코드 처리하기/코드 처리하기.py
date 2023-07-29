def solution(code):
    answer = ''
    
    mode = 0
    for index,value in enumerate(code):
        
        if mode == 0:
            if value == '1':
                mode = 1
            else:
                if index % 2 == 0:
                    answer += value
        elif mode == 1: 
            if value == '1':
                mode = 0
            else:
                if index % 2 != 0:
                    answer += value
        
    if answer == '':
            answer = 'EMPTY'
        
    return answer