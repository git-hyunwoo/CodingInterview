def solution(n):
    answer = 0
    
    if n % 2 == 0: 
        # 짝수일 경우
        for number in range(1, n + 1):
            if number % 2 == 0:
                answer += number ** 2
    else:
        # 홀수일 경우
        for number in range(1, n + 1):
            if number % 2 != 0:
                answer += number
    
    return answer