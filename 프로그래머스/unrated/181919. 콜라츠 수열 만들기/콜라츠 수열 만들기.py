def solution(n):
    answer = []
    while n != 1:
        
        if n % 2 == 0:
            # 짝수일 경우
            answer.append(n)
            n = n / 2
        else:
            # 홀수일 경우
            answer.append(n)
            n = 3 * n + 1
            
    answer.append(1)
        
    return answer