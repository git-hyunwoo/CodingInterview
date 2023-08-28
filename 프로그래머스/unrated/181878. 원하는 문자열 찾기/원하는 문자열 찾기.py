def solution(myString, pat):
    answer = 0
    
    myString = myString.upper()
    pat = pat.upper()
    
    if pat in myString:
        answer = 1
    return answer