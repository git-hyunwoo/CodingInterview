def solution(intStrs, k, s, l):
    answer = []
    
    for number in intStrs:
        if int(number[s:s + l]) > k:
            answer.append(int(number[s:s + l]))
    
    return answer