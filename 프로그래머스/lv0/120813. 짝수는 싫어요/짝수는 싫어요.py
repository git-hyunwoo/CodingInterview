def solution(n):
    answer = []
    for value in range(1,n + 1):
        if value % 2 != 0:
            answer.append(value)
    return answer