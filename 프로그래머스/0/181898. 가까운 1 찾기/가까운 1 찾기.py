def solution(arr, idx):
    answer = -1
    for index, value in enumerate(arr):
        if index >= idx and value == 1:
            answer = index
            break
    return answer