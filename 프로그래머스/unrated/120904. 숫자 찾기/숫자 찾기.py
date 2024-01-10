def solution(num, k):
    answer = -1
    num = [int(x) for x in str(num)]
    for index, value in enumerate(num):
        if value == k:
            answer = index + 1
            break
    return answer