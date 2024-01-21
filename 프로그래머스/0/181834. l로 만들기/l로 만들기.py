def solution(myString):
    answer = ''
    for value in myString:
        if ord(value) < ord('l'):
            answer += 'l'
        else:
            answer += value
    return answer