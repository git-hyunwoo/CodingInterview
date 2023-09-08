def solution(n, k):
    answer = []
    for value in range(1, n + 1):
        if value % k == 0:
            answer.append(value)
    return answer