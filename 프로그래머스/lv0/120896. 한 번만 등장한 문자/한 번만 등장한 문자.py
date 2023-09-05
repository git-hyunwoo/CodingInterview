def solution(s):
    answer = ''
    passed = []
    for value in s:
        if s.count(value) == 1 and value not in passed:
            answer += value
            passed.append(value)
            
    answer = ''.join(sorted(answer))
            
    return answer