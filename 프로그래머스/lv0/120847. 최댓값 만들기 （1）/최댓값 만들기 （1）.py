def solution(numbers):
    answer = 0
    numbers.sort()
    print(numbers)
    first_max = numbers[-1]
    second_max = numbers[-2]
    answer = first_max * second_max
    return answer