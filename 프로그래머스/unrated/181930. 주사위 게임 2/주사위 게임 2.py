def solution(a, b, c):
    answer = 0
    
    lst = list(map(int,''.join(str(a) + str(b) + str(c))))
    print(lst)
    
    if lst.count(a) == len(lst):
        # 3개 모두 같다면
        answer = (a + b + c) * (pow(a,2) + pow(b,2) + pow(c,2)) * (pow(a,3) + pow(b,3) + pow(c,3))
    else:
        if lst.count(a) == 2 or lst.count(b) == 2 or lst.count(c) == 2:
            # 2개가 같다면
            answer = (a + b + c) * (pow(a,2) + pow(b,2) + pow(c,2))
        else:
            # 3개 모두 다르다면
            answer = a + b + c
        
    
    return answer