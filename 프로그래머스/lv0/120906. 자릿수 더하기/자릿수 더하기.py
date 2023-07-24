def solution(n):
    
    answer = 0
    리스트 = list(map(int,str(n)))    
    for 숫자 in 리스트:
        answer += 숫자
        
    return answer