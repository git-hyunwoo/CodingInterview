def solution(myString):
    answer = []
    
    arr = myString.split('x')
    for value in arr:
        answer.append(len(value))
               
    return answer