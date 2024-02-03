def solution(myString):
    answer = ''
    myString = myString.lower()
    for alphabet in myString:
        if alphabet == 'a':
            answer += 'A'
        else:
            answer += alphabet
    return answer