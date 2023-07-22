def solution(left, right):
    answer = 0
    
    for n in range(left,right + 1):
        count = 0
        for x in range(1,n + 1):
            if n % x == 0:
                count += 1
                
        if count % 2 == 0:
            # 약수의 개수가 짝수일 경우 양수로 더하기
            answer += n
        else:
            # 약수의 개수가 홀수일 경우 음수로 더하기
            answer += n * -1
            
         
    return answer