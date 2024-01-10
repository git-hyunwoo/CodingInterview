# 오른쪽으로 1칸 이동
def right_shift(arr):
    arr = arr[-1:] + arr[:-1]
    return arr

# 왼쪽으로 1칸 이동
def left_shift(arr):
    arr = arr[1:] + arr[:1]
    return arr

def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer = right_shift(numbers)
    else:
        answer = left_shift(numbers)
    return answer