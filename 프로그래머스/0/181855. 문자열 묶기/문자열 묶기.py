def solution(strArr):
    answer = 0
    lst = [len(x) for x in strArr]
    
    numbers = []
    for number in range(1,max(lst) + 1):
        cnt = lst.count(number)
        numbers.append(cnt)
    
    answer = max(numbers)
        
    return answer