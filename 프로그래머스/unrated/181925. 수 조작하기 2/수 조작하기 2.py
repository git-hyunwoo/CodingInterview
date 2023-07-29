def solution(numLog):
    answer = ''
    
    for index,value in enumerate(numLog):
        
        if index != len(numLog) - 1:
            if value + 1 == numLog[index + 1]:
                # w
                answer += 'w'
            elif value - 1 == numLog[index + 1]:
                # s
                answer += 's'
            elif value + 10 == numLog[index + 1]:
                # d
                answer += 'd'
            elif value - 10 == numLog[index + 1]:
                # a
                answer += 'a'
            else:
                raise Exception("WARNING : only the letter w,s,d,a are available.")
    
    print(answer)
                    
    return answer