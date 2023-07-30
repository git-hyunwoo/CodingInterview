def solution(numbers, n):
    answer = 0
    for value in numbers:
        answer += value
        print(answer)
        if answer > n:
            break
            
    return answer