def solution(n):
    answer = []
    for value in range(1,n + 1):
        if n % value == 0:
            answer.append(value)
    return answer