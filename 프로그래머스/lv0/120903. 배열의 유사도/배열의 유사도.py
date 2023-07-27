def solution(s1, s2):
    answer = 0
    for letter in s1:
        if letter in s2:
            answer += 1
    return answer